#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains functions to workf with Ziva tissues
"""

from __future__ import print_function, division, absolute_import

import maya.cmds
import maya.mel


def is_tissue(mesh):
    """
    Returns whether or not given mesh is a Ziva Tissue mesh or not
    :param mesh: str, name of a mesh node
    :return: bool
    """

    maya.cmds.select(clear=True)
    ziva_tissue = maya.mel.eval('zQuery -type "zTissue"')
    if not ziva_tissue:
        return False

    return True
