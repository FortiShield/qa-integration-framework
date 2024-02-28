# Copyright (C) 2024, FortiShield Inc.
# Created by FortiShield, Inc. <security@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os
import sys

from fortishield_testing.constants.platforms import WINDOWS

from . import FORTISHIELD_PATH


VAR_PATH = os.path.join(FORTISHIELD_PATH, 'var')
VAR_RUN_PATH = os.path.join(VAR_PATH, 'run')

ANALYSISD_STATE = os.path.join(VAR_RUN_PATH, 'fortishield-analysisd.state')

if sys.platform == WINDOWS:
    VERSION_FILE = os.path.join(FORTISHIELD_PATH, 'VERSION')
    AGENTD_STATE = os.path.join(FORTISHIELD_PATH, 'fortishield-agent.state')
else:
    VERSION_FILE = ''
    AGENTD_STATE = os.path.join(VAR_RUN_PATH, 'fortishield-agentd.state')

VAR_MULTIGROUPS_PATH = os.path.join(VAR_PATH, 'multigroups')
