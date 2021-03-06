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

"""Handles all requests relating to OperationEngine."""


from oslo_config import cfg
from oslo_log import log as logging

from smaug.db import base
from smaug.services.operationengine import rpcapi as operationengine_rpcapi


CONF = cfg.CONF

LOG = logging.getLogger(__name__)


class API(base.Base):
    """API for interacting with the OperationEngine manager."""

    def __init__(self, db_driver=None):
        self.operationengine_rpcapi = operationengine_rpcapi.\
            OperationEngineAPI()
        super(API, self).__init__(db_driver)

    def create_scheduled_operation(self, context, operation_id, trigger_id):
        self.operationengine_rpcapi.create_scheduled_operation(
            context, operation_id, trigger_id)

    def delete_scheduled_operation(self, context, operation_id, trigger_id):
        self.operationengine_rpcapi.delete_scheduled_operation(
            context, operation_id, trigger_id)

    def create_trigger(self, context, trigger):
        self.operationengine_rpcapi.create_trigger(context, trigger)

    def delete_trigger(self, context, trigger_id):
        self.operationengine_rpcapi.delete_trigger(context, trigger_id)

    def update_trigger(self, context, trigger):
        self.operationengine_rpcapi.update_trigger(context, trigger)
