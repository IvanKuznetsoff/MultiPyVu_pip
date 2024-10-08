# -*- coding: utf-8 -*-
"""
This file contains several variables which are used throughout the project.

Created on Mon Sep 27 10:53:06 2021

@author: D. Jackson
"""

from sys import platform
import os
import distutils.sysconfig
from importlib.metadata import version
from .exceptions import PythoncomImportError


py_win_version = 0.0
if platform == 'win32':
    try:
        import win32com.client as win32
    except ImportError:
        raise PythoncomImportError

    # Get the version number for pywin32
    # the version number is usually an int, but sometimes
    # it is a fraction, so convert to a float
    py_win_version = float(version('pywin32'))
PYWIN32_VERSION = py_win_version


HOST = 'localhost'
# non-privileged ports are 1023 < 65535
PORT = 5000

TIMEOUT_LENGTH = 1.0
SERVER_NAME = 'MultiVuServer'
CLIENT_NAME = 'MultiVuClient'

MIN_PYWIN32_VERSION = 300

LOG_NAME = 'QdMultiVu.log'
