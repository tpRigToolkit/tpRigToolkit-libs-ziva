#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpRigToolkit-libs-ziva
"""

from __future__ import print_function, division, absolute_import

import os
import sys
import logging.config

from tpDcc.core import library
from tpDcc.libs.python import path as path_utils

from tpRigToolkit.libs.ziva.core import consts


class ZivaLib(library.DccLibrary, object):

    ID = consts.LIB_ID

    def __init__(self, *args, **kwargs):
        super(ZivaLib, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls):
        base_tool_config = library.DccLibrary.config_dict()
        tool_config = {
            'name': 'Ziva Library',
            'id': cls.ID,
            'supported_dccs': {'maya': ['2017', '2018', '2019', '2020']},
            'tooltip': 'Library to Ziva data'
        }
        base_tool_config.update(tool_config)

        return base_tool_config

    @classmethod
    def load(cls):
        ziva_utils_folder = path_utils.clean_path(
            os.path.join(os.path.dirname(os.path.dirname(__file__)), '__scripts__', 'ziva-vfx-utils'))
        if os.path.isdir(ziva_utils_folder) and ziva_utils_folder not in sys.path:
            sys.path.append(ziva_utils_folder)


def create_logger(dev=False):
    """
    Creates logger for current tpDcc-libs-resources package
    """

    logger_directory = os.path.normpath(os.path.join(os.path.expanduser('~'), 'tpDcc', 'logs', 'libs'))
    if not os.path.isdir(logger_directory):
        os.makedirs(logger_directory)

    logging_config = os.path.normpath(os.path.join(os.path.dirname(os.path.dirname(__file__)), '__logging__.ini'))

    logging.config.fileConfig(logging_config, disable_existing_loggers=False)
    logger = logging.getLogger('tpRigToolkit-libs-ziva')
    dev = os.getenv('TPRIGTOOLKIT_DEV', dev)
    if dev:
        logger.setLevel(logging.DEBUG)
        for handler in logger.handlers:
            handler.setLevel(logging.DEBUG)

    return logger


create_logger()
