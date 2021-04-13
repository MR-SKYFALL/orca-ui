# Copyright 2020 OpenRCA Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask_restx import Namespace, Resource

from orca_mock import mock_data

namespace = Namespace('rca', description='RCA API')


@namespace.route('/')
class RCA(Resource):

    def __init__(self, _api):
        super().__init__()
        self._mock_data = mock_data.load_data('rca')

    def get(self):
        return self._mock_data

