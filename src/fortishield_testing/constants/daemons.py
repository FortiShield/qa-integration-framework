# Copyright (C) 2024, FortiShield Inc.
# Created by FortiShield, Inc. <security@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

AGENT_DAEMON = 'fortishield-agentd'
AGENTLESS_DAEMON = 'fortishield-agentlessd'
ANALYSISD_DAEMON = 'fortishield-analysisd'
API_DAEMON = 'fortishield-apid'
AUTHD_DAEMON = 'fortishield-authd'
CLUSTER_DAEMON = 'fortishield-clusterd'
CSYSLOG_DAEMON = 'fortishield-csyslogd'
EXEC_DAEMON = 'fortishield-execd'
INTEGRATOR_DAEMON = 'fortishield-integratord'
MAIL_DAEMON = 'fortishield-maild'
MODULES_DAEMON = 'fortishield-modulesd'
MONITOR_DAEMON = 'fortishield-monitord'
LOGCOLLECTOR_DAEMON = 'fortishield-logcollector'
REMOTE_DAEMON = 'fortishield-remoted'
SYSCHECK_DAEMON = 'fortishield-syscheckd'
FORTISHIELD_DB_DAEMON = 'fortishield-db'

FORTISHIELD_AGENT_DAEMONS = [AGENT_DAEMON,
                       EXEC_DAEMON,
                       MODULES_DAEMON,
                       LOGCOLLECTOR_DAEMON,
                       SYSCHECK_DAEMON]

FORTISHIELD_MANAGER_DAEMONS = [AGENTLESS_DAEMON,
                         ANALYSISD_DAEMON,
                         API_DAEMON,
                         CLUSTER_DAEMON,
                         CSYSLOG_DAEMON,
                         EXEC_DAEMON,
                         INTEGRATOR_DAEMON,
                         LOGCOLLECTOR_DAEMON,
                         MAIL_DAEMON,
                         MODULES_DAEMON,
                         MONITOR_DAEMON,
                         REMOTE_DAEMON,
                         SYSCHECK_DAEMON,
                         FORTISHIELD_DB_DAEMON]

API_DAEMONS_REQUIREMENTS = [API_DAEMON,
                            FORTISHIELD_DB_DAEMON,
                            EXEC_DAEMON,
                            ANALYSISD_DAEMON,
                            REMOTE_DAEMON,
                            MODULES_DAEMON]

FORTISHIELD_AGENT = 'fortishield-agent'
FORTISHIELD_MANAGER = 'fortishield-manager'

FORTISHIELD_AGENT_WIN = 'fortishield-agent.exe'
