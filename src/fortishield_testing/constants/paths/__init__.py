# Copyright (C) 2024, FortiShield Inc.
# Created by FortiShield, Inc. <security@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import sys
import os

from fortishield_testing.constants.platforms import MACOS, WINDOWS

TEMP_FILE_PATH = '/tmp'

if sys.platform == WINDOWS:
    FORTISHIELD_PATH = os.path.join("C:", os.sep, "Program Files (x86)", "ossec-agent")
    ROOT_PREFIX = os.path.join('c:', os.sep)

elif sys.platform == MACOS:
    FORTISHIELD_PATH = os.path.join("/", "Library", "Ossec")
    ROOT_PREFIX = os.path.join('/', 'private', 'var', 'root')

else:
    FORTISHIELD_PATH = os.path.join("/", "var", "ossec")
    ROOT_PREFIX = os.sep
