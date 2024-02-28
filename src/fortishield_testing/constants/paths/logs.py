# Copyright (C) 2024, FortiShield Inc.
# Created by FortiShield, Inc. <security@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os
import sys

from fortishield_testing.constants.platforms import WINDOWS

from . import FORTISHIELD_PATH


BASE_LOGS_PATH = os.path.join(FORTISHIELD_PATH, 'logs')

if sys.platform == WINDOWS:
    BASE_LOGS_PATH = FORTISHIELD_PATH
    ACTIVE_RESPONSE_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'active-response', 'active-responses.log')
else:
    ACTIVE_RESPONSE_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'active-responses.log')

FORTISHIELD_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'ossec.log')
ALERTS_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'alerts', 'alerts.log')
ALERTS_JSON_PATH = os.path.join(BASE_LOGS_PATH, 'alerts', 'alerts.json')
ARCHIVES_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'archives', 'archives.log')
ARCHIVES_JSON_PATH = os.path.join(BASE_LOGS_PATH, 'archives', 'archives.json')

# API logs paths
FORTISHIELD_API_LOG_FILE_PATH = os.path.join(BASE_LOGS_PATH, 'api.log')
FORTISHIELD_API_JSON_LOG_FILE_PATH = os.path.join(BASE_LOGS_PATH, 'api.json')

FORTISHIELD_CLUSTER_LOGS_PATH = os.path.join(BASE_LOGS_PATH, 'cluster.log')
