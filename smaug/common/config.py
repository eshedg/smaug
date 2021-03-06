#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Command-line flag library.

Emulates gflags by wrapping cfg.ConfigOpts.

The idea is to move fully to cfg eventually, and this wrapper is a
stepping stone.

"""

import socket

from oslo_config import cfg
from oslo_log import log as logging


CONF = cfg.CONF
logging.register_options(CONF)

core_opts = [
    cfg.StrOpt('api_paste_config',
               default="api-paste.ini",
               help='File name for the paste.deploy config for smaug-api'),
    cfg.StrOpt('state_path',
               default='/var/lib/smaug',
               deprecated_name='pybasedir',
               help="Top-level directory for maintaining smaug's state"),
]

debug_opts = [
]

CONF.register_cli_opts(core_opts)
CONF.register_cli_opts(debug_opts)

global_opts = [
    cfg.IntOpt('service_down_time',
               default=60,
               help='Maximum time since last check-in for a service to be '
                    'considered up'),
    cfg.StrOpt('operationengine_topic',
               default='smaug-operationengine',
               help='The topic that OperationEngine nodes listen on'),
    cfg.StrOpt('operationengine_manager',
               default='smaug.services.operationengine.manager.'
               'OperationEngineManager',
               help='Full class name for the Manager for OperationEngine'),
    cfg.StrOpt('protection_topic',
               default='smaug-protection',
               help='The topic that protection nodes listen on'),
    cfg.StrOpt('protection_manager',
               default='smaug.services.protection.manager.ProtectionManager',
               help='Full class name for the Manager for Protection'),
    cfg.StrOpt('host',
               default=socket.gethostname(),
               help='Name of this node.  This can be an opaque identifier. '
                    'It is not necessarily a host name, FQDN, or IP address.'),
    cfg.StrOpt('auth_strategy',
               default='keystone',
               choices=['noauth', 'keystone'],
               help='The strategy to use for auth. Supports noauth or '
                    'keystone.'),
]

CONF.register_opts(global_opts)
