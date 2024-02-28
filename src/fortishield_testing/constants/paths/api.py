"""
Copyright (C) 2024, FortiShield Inc.
Created by FortiShield, Inc. <security@khulnasoft.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
import os

from . import FORTISHIELD_PATH

# API paths that do not fit in `configurations`

# Folders
FORTISHIELD_API_FOLDER_PATH = os.path.join(FORTISHIELD_PATH, 'api')
FORTISHIELD_API_CONFIGURATION_FOLDER_PATH = os.path.join(FORTISHIELD_API_FOLDER_PATH, 'configuration')
FORTISHIELD_API_SECURITY_FOLDER_PATH = os.path.join(FORTISHIELD_API_CONFIGURATION_FOLDER_PATH, 'security')
FORTISHIELD_API_SCRIPTS_FOLDER_PATH = os.path.join(FORTISHIELD_API_FOLDER_PATH, 'scripts')

# API scripts paths
FORTISHIELD_API_SCRIPT = os.path.join(FORTISHIELD_API_SCRIPTS_FOLDER_PATH, 'fortishield-apid.py')

# Databases paths
RBAC_DATABASE_PATH = os.path.join(FORTISHIELD_API_SECURITY_FOLDER_PATH, 'rbac.db')

# SSL paths
FORTISHIELD_API_CERTIFICATE = os.path.join(FORTISHIELD_API_CONFIGURATION_FOLDER_PATH, 'ssl', 'server.crt')
