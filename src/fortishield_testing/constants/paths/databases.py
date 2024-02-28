# Copyright (C) 2024, FortiShield Inc.
# Created by FortiShield, Inc. <security@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os
from . import FORTISHIELD_PATH


CVE_DB_PATH = os.path.join(FORTISHIELD_PATH, 'queue', 'vulnerabilities', 'cve.db')
CPE_HELPER_PATH = os.path.join(FORTISHIELD_PATH, 'queue', 'vulnerabilities', 'dictionaries', 'cpe_helper.json')
