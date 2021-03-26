#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains Ziva rig data part implementation
"""

from __future__ import print_function, division, absolute_import

import os
import re
import logging

# from zBuilder.builders import ziva

from tpDcc.core import dcc as core_dcc
from tpDcc.libs.datalibrary.core import datapart

from tpRigToolkit.libs.ziva.core import consts

logger = logging.getLogger(consts.LIB_ID)


class ZivaRigData(datapart.DataPart):

    DATA_TYPE = 'maya.zivarig'
    MENU_ICON = 'ziva'
    MENU_NAME = 'Ziva Rig'
    PRIORITY = 15
    EXTENSION = '.zBuilder'

    _has_trait = re.compile(r'\.zBuilder', re.I)

    @classmethod
    def can_represent(cls, identifier, only_extension=False):
        if ZivaRigData._has_trait.search(identifier):
            if only_extension:
                return True
            if os.path.isfile(identifier):
                return True

        return False

    @classmethod
    def supported_dccs(cls):
        return [core_dcc.Dccs.Maya]

    def label(self):
        return os.path.basename(self.identifier())

    def icon(self):
        return 'ziva'

    def extension(self):
        return '.zBuilder'

    def type(self):
        return 'maya.zivarig'

    def menu_name(self):
        return 'Ziva Rig'

    def functionality(self):
        return dict(
            import_data=self.import_data,
            export_data=self.export_data,
            save=self.save
        )

    def import_data(self):
        """
        Imports Ziva Rig file into current Maya scene
        """

        filepath = self.format_identifier()
        if not filepath or not os.path.isfile(filepath):
            return

        ziva_rig = ziva.Ziva()
        ziva_rig.retrieve_from_file(filepath)
        return ziva_rig.build()

    def export_data(self, *args, **kwargs):
        return self.save(*args, **kwargs)

    def save(self, *args, **kwargs):
        """
        Saves Ziva Rig file
        """

        filepath = self.format_identifier()
        if not filepath:
            logger.warning('Impossible to save Ziva rig file because save file path not defined!')
            return

        logger.debug('Saving {} | {}'.format(filepath, kwargs))

        ziva_rig = ziva.Ziva()
        ziva_rig.retrieve_from_scene()
        result = ziva_rig.write(filepath)

        logger.debug('Saved {} successfully!'.format(filepath))

        return result
