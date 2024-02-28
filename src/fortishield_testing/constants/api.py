"""
Copyright (C) 2024, FortiShield Inc.
Created by FortiShield, Inc. <security@khulnasoft.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
# API basic information
CONFIGURATION_TYPES = ('base', 'security')
FORTISHIELD_API_PROTOCOL = 'https'
FORTISHIELD_API_HOST = 'localhost'
FORTISHIELD_API_PORT = '55000'
FORTISHIELD_API_USER = 'fortishield'
FORTISHIELD_API_PASSWORD = 'fortishield'

# API routes
LOGIN_ROUTE = '/security/user/authenticate'
RULES_FILES_ROUTE = '/rules/files'
AGENTS_ROUTE = '/agents'
SYSCOLLECTOR_OS_ROUTE = '/experimental/syscollector/os'
MANAGER_CONFIGURATION_ROUTE = '/manager/configuration'
MANAGER_INFORMATION_ROUTE = '/manager/info'
GROUPS_ROUTE = '/groups'
CDB_LIST_ROUTE = '/lists/files'
DAEMONS_STATS_ROUTE = '/manager/daemons/stats'
# RBAC routes
USERS_ROUTE = '/security/users'
ROLES_ROUTE = '/security/roles'
POLICIES_ROUTE = '/security/policies'
RULES_ROUTE = '/security/rules'
RESOURCE_ROUTE_MAP = {
    'user_ids': USERS_ROUTE,
    'role_ids': ROLES_ROUTE,
    'policy_ids': POLICIES_ROUTE,
    'rule_ids': RULES_ROUTE
}
TARGET_ROUTE_MAP = {
    'user_ids': 'users',
    'role_ids': 'roles',
    'policy_ids': 'policies',
    'rule_ids': 'rules'
}
