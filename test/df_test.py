# -*- coding: utf-8 -*-
# Copyright (c) 2013 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
import re
from minicluster import MiniClusterTestBase


class DfTest(MiniClusterTestBase):

    def test_df(self):
        client_output = self.client.df()[0]
        expected_output = self.cluster.df("/").split("\n")[1]

        print client_output
        print expected_output
        (filesystem, capacity, used, remaining, pct) = re.split("\s+", expected_output)

        self.assertEqual(filesystem, client_output["filesystem"])
        self.assertEqual(long(capacity), client_output["capacity"])
        self.assertEqual(long(used), client_output["used"])