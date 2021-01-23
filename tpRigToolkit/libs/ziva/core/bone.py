#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains functions to work with Ziva bones
"""

from __future__ import print_function, division, absolute_import

import maya.cmds
import maya.mel


def is_bone(mesh):
    """
    Returns whether or not given mesh is a Ziva Bone mesh or not
    :param mesh: str, name of a mesh node
    :return: bool
    """

    maya.cmds.select(clear=True)
    ziva_tissue = maya.mel.eval('zQuery -type "zBone"')
    if not ziva_tissue:
        return False

    return True
