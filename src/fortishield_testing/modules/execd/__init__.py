# Copyright (C) 2024, FortiShield Inc.
# Created by FortiShield, Inc. <security@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

import sys

from fortishield_testing.constants.platforms import WINDOWS


if sys.platform == WINDOWS:
    PREFIX = r'.*execd.*'
else:
    PREFIX = r'.*fortishield-execd.*'
