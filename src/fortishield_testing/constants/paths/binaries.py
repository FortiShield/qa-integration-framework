# Copyright (C) 2024, FortiShield Inc.
# Created by FortiShield, Inc. <security@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os
import sys

from fortishield_testing.constants.platforms import WINDOWS

from . import FORTISHIELD_PATH

if sys.platform == WINDOWS:
    BIN_PATH = FORTISHIELD_PATH
else:
    BIN_PATH = os.path.join(FORTISHIELD_PATH, 'bin')

FORTISHIELD_CONTROL_PATH = os.path.join(BIN_PATH, 'fortishield-control')
AGENT_AUTH_PATH = os.path.join(BIN_PATH, 'agent-auth')
ACTIVE_RESPONSE_BIN_PATH = os.path.join(FORTISHIELD_PATH, 'active-response', 'bin')
ACTIVE_RESPONSE_FIREWALL_DROP = os.path.join(ACTIVE_RESPONSE_BIN_PATH, 'firewall-drop')
MANAGE_AGENTS_BINARY = os.path.join(BIN_PATH, 'manage_agents')
AGENT_GROUPS_BINARY = os.path.join(BIN_PATH, 'agent_groups')
