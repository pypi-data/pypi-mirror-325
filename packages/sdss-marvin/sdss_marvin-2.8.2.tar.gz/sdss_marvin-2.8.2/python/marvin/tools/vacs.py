# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Filename: vacs.py
# Project: tools
# Author: Brian Cherinka
# Created: Sunday, 8th September 2019 11:16:35 pm
# License: BSD 3-clause "New" or "Revised" License
# Copyright (c) 2019 Brian Cherinka
# Last Modified: Tuesday, 3rd December 2019 2:43:32 pm
# Modified By: Brian Cherinka


from __future__ import print_function, division, absolute_import
import contextlib
import inspect
import six
import os
import importlib
import types
import numpy as np
from marvin.contrib.vacs.base import VACContainer, VACMixIn
from marvin import config, log
from marvin.core.exceptions import MarvinError
from marvin.utils.general import parseIdentifier, get_drpall_table
from decorator import decorator

from astropy.io import fits
from astropy.table import Table

import sdss_access.sync


def check_release(*args, **kwargs):
    ''' Decorator to check VAC release against Marvin config release  '''
    @decorator
    def decorated_function(ff, *args, **kwargs):
        inst = args[0]
        if inst.release != config.release:
            raise AssertionError('Mismatch between VAC release and current Marvin release.'
                                 'Please reinstantiate your VACs.')

        return ff(*args, **kwargs)
    return decorated_function


class check_vac_release(object):
    ''' Decorate all functions in a class to run only if VAC release matches Marvin release '''

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, decorated_class):
        for attr in inspect.getmembers(decorated_class, inspect.isfunction):
            # only decorate public functions
            if attr[0][0] != '_':
                setattr(decorated_class, attr[0],
                        check_release(*self.args, **self.kwargs)(getattr(decorated_class, attr[0])))
        return decorated_class


@check_vac_release()
class VACs(VACContainer):
    ''' A class to interface with the MaNGA VACs

    A container class to interact with all MaNGA VACs that
    have been contributed into Marvin.  Currently, this container
    only works with local VACs.  Remote-only access to VACs currently
    does not exist.

    Attributes:
        release (str):
            The current MPL/DR version of the loaded VACs
        vacname (object):
            A specific VAC object.  "vacname" is the name of the VAC, e.g. galaxyzoo

    Example:
        >>> from marvin.tools.vacs import VACs
        >>> vacs = VACs()
    '''

    @classmethod
    def _reset_vacs(cls):
        ''' reset the VAC class to a blank slate '''
        if hasattr(cls, '_vacs'):
            for vac in cls._vacs:
                # close the HDU file resource
                vv = getattr(cls, vac)
                if hasattr(vv, '_data') and getattr(vv, '_data') is not None:
                    vv._data.close()
                # delete the attribute
                delattr(cls, vac)

    def __new__(cls, *args, **kwargs):
        ''' load relevant VACMixIns upon new class creation '''
        # reset the vacs
        cls._reset_vacs()
        # initiate vacs for a given release
        cls._vacs = []
        cls.release = config.release
        for subvac in VACMixIn.__subclasses__():
            # Exclude any hidden VACs
            if subvac._hidden and (not subvac._hidden_for or 
                                   (subvac._hidden_for == cls.release)):
                continue

            # Excludes VACs from other releases
            if config.release not in subvac.version:
                continue

            sv = subvac()
            if sv.summary_file is None:
                log.info('VAC {0} has no summary file to load.  Skipping.'.format(sv.name))
                continue

            # create the VAC data class
            if isinstance(sv.summary_file, list):
                # return a list of data classes if multiple summary files are provided
                if sv.data_container and type(sv.data_container) is dict:
                    # use any data container if provided
                    vacdc = {k: VACDataClass(subvac.name, subvac.description, v, 
                                             display_name=subvac.display_name, url=subvac.url) for k, v in sv.data_container.items()}
                else:
                    vacdc = [VACDataClass(subvac.name, subvac.description, s, 
                                          display_name=subvac.display_name, url=subvac.url) for s in sv.summary_file]
                    if len(vacdc) == 1:
                        vacdc = vacdc[0]
            elif isinstance(sv.summary_file, str):
                vacdc = VACDataClass(subvac.name, subvac.description, sv.summary_file, display_name=subvac.display_name, url=subvac.url)

            # add any custom methods to the VAC
            if hasattr(subvac, 'add_methods'):
                for method in getattr(subvac, 'add_methods'):
                    assert isinstance(method, six.string_types), 'method name must be a string'
                    svmod = importlib.import_module(subvac.__module__)
                    assert hasattr(svmod, method), 'method name must be defined in VAC module file'
                    setattr(vacdc, method, types.MethodType(
                        getattr(svmod, method), vacdc))

            # add vac to the container class
            cls._vacs.append(subvac.name)
            setattr(cls, subvac.name, vacdc)

        return super(VACs, cls).__new__(cls, *args, **kwargs)

    def __repr__(self):
        ''' repr for VAC container '''
        n_vacs = len(self._vacs)
        if n_vacs <= 7:
            return '<VACs ({0})>'.format(', '.join(self._vacs))
        return '<VACs (n_vacs={0})>'.format(n_vacs)

    def list_vacs(self):
        ''' list the available VACS '''
        return self._vacs

    def check_target(self, target, lomem=None):
        ''' check which VACS a MaNGA target is available in

        Checks for the target in each VAC and returns a
        dictionary of VAC names and a boolean indicating
        if the target is in that VAC

        Parameters:
            target (str):
                The name of the target
            lomem (str):
                If True, loads the data via context manager

        Returns:
            A dict of booleans
        '''
        vacs = {}
        for vac in self._vacs:
            if isinstance(self[vac], VACDataClass):
                vacs[vac] = self[vac].has_target(target, lomem=lomem)
            elif isinstance(self[vac], dict):
                vacs[vac] = {k: v.has_target(target, lomem=lomem) for k, v in self[vac].items()}
            elif isinstance(self[vac], list):
                vacs[vac] = [v.has_target(target, lomem=lomem) for v in self[vac]]
        return vacs
    
    def match_targets(self, targets: list = None, to_df: bool = True):
        """ Match a list of mangaid targets across all VACs

        Check a list of mangaid targets against all VACs and return a Pandas
        DataFrame (default) or a dictionary of booleans indicating which mangaids
        are in which VACs.  If no targets are provided, all targets from the 
        DRPall file of the currently set release will be checked.

        Parameters
        ----------
        targets : list, optional
            A list of mangaids, by default None
        to_df : bool, optional
            If True converts the dictionary to a pandas dataframe, by default True

        Returns
        -------
        pandas.DataFrame or dict
            Booleans indicating which mangaids are in which VACs

        Raises
        ------
        ValueError
            when targets is not a list
        ValueError
            when the targets are not a mangaid
        """

        if not targets:
            drpver, __ = config.lookUpVersions(self.release)
            targets = get_drpall_table(drpver)['mangaid'].tolist()

        if not isinstance(targets, list):
            raise ValueError('targets must be a list')

        # check target
        targtype = parseIdentifier(targets[0])
        if targtype != 'mangaid':
            raise ValueError('targets must be mangaids')

        vtargs = {"release": [self.release] * len(targets), "mangaid": targets}
        for vac in self._vacs:
            if isinstance(self[vac], VACDataClass):
                mm = self[vac].get_mangaids()
                vtargs[vac] = np.isin(targets, mm)
            elif isinstance(self[vac], dict):
                for kk, vv in self[vac].items():
                    vtargs[f'{vac}_{kk}'] = np.isin(targets, vv.get_mangaids())
            elif isinstance(self[vac], list):
                for ii, ee in enumerate(self[vac]):
                    vtargs[f'{vac}_{ii}'] = np.isin(targets, ee.get_mangaids())
        
        # by default convert to a pandas dataframe
        if to_df:
            import pandas as pd
            return pd.DataFrame.from_dict(vtargs)
        return vtargs

class VACDataClass(object):
    ''' A data class for a given VAC

    Parameters:
        name (str):
            The name of the VAC
        description (str):
            The description of the VAC
        path (str):
            The full path to the VAC summary file
        display_name (str):
            The display name of the VAC
        url (str):
            The URL to the VAC description page

    Attributes:
        name (str):
            The name of the VAC
        description (str):
            The description of the VAC
        data (HDUList):
            The Astropy FITS HDUList
        display_name (str):
            The display name of the VAC
        url (str):
            The URL to the VAC description page

    Example:
        >>> from marvin.tools.vacs import VACs
        >>> vacs = VACs()
        >>> vacs.galaxyzoo.data
        >>> vacs.galaxyzoo.get_table(ext=1)
    '''
    def __init__(self, name, description, path, display_name=None, url=None):
        self.name = name
        self.description = description
        self.display_name = display_name
        self.url = url
        self._path = path
        self._data = None

        if not sdss_access.sync.Access:
            raise MarvinError('sdss_access is not installed')
        else:
            self._rsync = sdss_access.sync.Access(release=config.release)

    def __repr__(self):
        name = self.name.title().replace('_', '')
        if not self._data:
            end = ''
        end = '' if not self._data else ', n_hdus={0}'.format(len(self.data))
        return '<{0}Data(description={1}{2})>'.format(name, self.description, end)

    @property
    def data(self):
        ''' The VAC FITS data '''
        if not self._data:
            self._check_file()
            self._data = fits.open(self._path)
        return self._data
    
    @contextlib.contextmanager
    def get_data(self, ext=1):
        ''' Get the data from a specific extension
        
        Context manager to return the data from a given extension.
        Useful for large FITS files that you don't want to load all at once.

        '''
        self._check_file()
        with fits.open(self._path) as hdulist:
            yield hdulist[ext].data
        del hdulist[ext].data
    
    def __del__(self):
        ''' Close the file on delete '''
        if self._data and isinstance(self._data, fits.HDUList):
            self._data.close()

    def info(self):
        ''' print the VAC HDU info '''
        self.data.info()

    def get_table(self, ext=None):
        ''' Create an Astropy table for a data extension

        Parameters:
            ext (int|str):
                The HDU extension name or number

        Returns:
            An Astropy table for the given extension
        '''
        if not ext:
            log.info('No HDU extension specified.  Defaulting to ext=1')
            ext = 1

        # check if extension is an image
        if self.data[ext].is_image:
            log.info('Ext={0} is not a table extension.  Cannot read.'.format(ext))
            return

        return Table.read(self._path, ext, format='fits')

    def download_vac(self):
        ''' Download a VAC to the local system '''
        if self._data:
            log.info('File already downloaded.')
            return

        log.info('Downloading VAC data..')
        self._rsync.reset()
        self._rsync.remote()
        self._rsync.add('', full=self._path)
        self._rsync.set_stream()
        self._rsync.commit()

    def _check_file(self):
        ''' check for a file locally, else downloads it '''

        # ensure file is of FITS format
        ext = os.path.splitext(self._path)[-1]
        assert '.fits' in ext, 'VAC summary file must be of FITS format'

        # download file
        if not self._rsync.exists('', full=self._path):
            self.download_vac()

    def has_target(self, target: str, lomem: bool = False) -> bool:
        ''' Checks if a target is contained within the VAC

        Checks if a target mangaid or plateifu is within the 
        first data extension of the VAC.  By default, uses the
        full data loaded into memory.  Use the lomem flag to
        instead load the data using a context manager.  This is useful
        for large FITS files in a low-memory environment, such as a web
        server.

        Parameters:
            target (str):
                The name of the target
            lomem (str):
                If True, loads the data via context manager

        Returns:
            A boolean indicating if the target is in the VAC or not
        '''
        assert isinstance(target, six.string_types), 'target must be a string'
        targ_type = parseIdentifier(target)
        ttypes = ['plateifu', 'mangaid']
        other = ttypes[ttypes.index(targ_type)-1]
        
        if not lomem:
            data = self.data[1].data
            assert targ_type in map(str.lower, data.columns.names), \
                'Identifier "{0}" is not available.  Try a "{1}".'.format(targ_type, other)
            return target in data[targ_type]

        with self.get_data(ext=1) as data:
            assert targ_type in map(str.lower, data.columns.names), \
                'Identifier "{0}" is not available.  Try a "{1}".'.format(targ_type, other)

            return target in data[targ_type]
        
    def get_mangaids(self, ext=1):
        """ Get the mangaids from the VAC """
        return self.data[ext].data['mangaid'].strip().tolist()
        
