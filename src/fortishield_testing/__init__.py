# Copyright (C) 2024, FortiShield Inc.
# Created by FortiShield, Inc. <security@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
from pathlib import Path

from . import global_parameters


DATA_PATH = Path(Path(__file__).parent, 'data')
FEEDS_PATH = Path(DATA_PATH, 'feeds')
SCRIPTS_PATH = Path(Path(__file__).parent, 'scripts')

session_parameters = global_parameters.GlobalParameters()
