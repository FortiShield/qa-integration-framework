# Copyright (C) 2024, FortiShield Inc.
# Created by FortiShield, Inc. <security@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os

from . import FORTISHIELD_PATH


QUEUE_CLUSTER_PATH = os.path.join(FORTISHIELD_PATH, 'queue', 'cluster')
QUEUE_DB_PATH = os.path.join(FORTISHIELD_PATH, 'queue', 'db')
QUEUE_SOCKETS_PATH = os.path.join(FORTISHIELD_PATH, 'queue', 'sockets')
QUEUE_AGENTS_TIMESTAMP_PATH = os.path.join(FORTISHIELD_PATH, 'queue', 'agents-timestamp')
QUEUE_DIFF_PATH = os.path.join(FORTISHIELD_PATH, 'queue', 'diff')
QUEUE_RIDS_PATH = os.path.join(FORTISHIELD_PATH, 'queue', 'rids')
QUEUE_ALERTS_PATH = os.path.join(FORTISHIELD_PATH, 'queue', 'alerts')

ANALYSISD_ANALISIS_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'analysis')
ANALYSISD_QUEUE_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'queue')
AUTHD_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'auth')
EXECD_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'com')
LOGCOLLECTOR_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'logcollector')
LOGTEST_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'logtest')
MODULESD_WMODULES_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'wmodules')
MODULESD_DOWNLOAD_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'download')
MODULESD_CONTROL_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'control')
MODULESD_KREQUEST_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'krequest')
MODULESD_C_INTERNAL_SOCKET_PATH = os.path.join(QUEUE_CLUSTER_PATH, 'c-internal.sock')
MONITORD_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'monitor')
REMOTED_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'remote')
SYSCHECKD_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'syscheck')
FORTISHIELD_DB_SOCKET_PATH = os.path.join(QUEUE_DB_PATH, 'wdb')
ACTIVE_RESPONSE_SOCKET_PATH = os.path.join(QUEUE_ALERTS_PATH, 'ar')


FORTISHIELD_SOCKETS = {
    'fortishield-agentd': [],
    'fortishield-apid': [],
    'fortishield-agentlessd': [],
    'fortishield-csyslogd': [],
    'fortishield-analysisd': [
        ANALYSISD_ANALISIS_SOCKET_PATH,
        ANALYSISD_QUEUE_SOCKET_PATH
    ],
    'fortishield-authd': [AUTHD_SOCKET_PATH],
    'fortishield-execd': [EXECD_SOCKET_PATH],
    'fortishield-logcollector': [LOGCOLLECTOR_SOCKET_PATH],
    'fortishield-monitord': [MONITORD_SOCKET_PATH],
    'fortishield-remoted': [REMOTED_SOCKET_PATH],
    'fortishield-maild': [],
    'fortishield-syscheckd': [SYSCHECKD_SOCKET_PATH],
    'fortishield-db': [FORTISHIELD_DB_SOCKET_PATH],
    'fortishield-modulesd': [
        MODULESD_WMODULES_SOCKET_PATH,
        MODULESD_DOWNLOAD_SOCKET_PATH,
        MODULESD_CONTROL_SOCKET_PATH,
        MODULESD_KREQUEST_SOCKET_PATH
    ],
    'fortishield-clusterd': [MODULESD_C_INTERNAL_SOCKET_PATH]
}

# These sockets do not exist with default FortiShield configuration
FORTISHIELD_OPTIONAL_SOCKETS = [
    MODULESD_KREQUEST_SOCKET_PATH,
    AUTHD_SOCKET_PATH
]
