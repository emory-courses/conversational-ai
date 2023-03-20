# ========================================================================
# Copyright 2023 Emory University
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
# ========================================================================

__author__ = 'Jinho D. Choi'

import re
import unittest
from re import Pattern

from src.regexutils import generate


class TestRegex(unittest.TestCase):
    def is_pass(self, regex: Pattern, input: str):
        m = regex.match(input)
        if not m: raise AssertionError
        self.assertEqual(m.group(), input)

    def is_fail(self, regex: Pattern, input: str):
        m = regex.match(input)
        if m: self.assertNotEqual(m.group(), input)

    def test_bool(self):
        r = re.compile(generate(True))
        self.is_pass(r, 'true')
        self.is_pass(r, 'false')
        self.is_fail(r, 'False')

    def test_str(self):
        r = re.compile(generate('hello'))
        self.is_pass(r, '"Who are you?"')
        self.is_pass(r, '"I\'m \\"Mike\\"."')
        self.is_fail(r, 'Good')

    def test_int(self):
        r = re.compile(generate(0))
        self.is_pass(r, '1')
        self.is_pass(r, '-10')

    def test_float(self):
        r = re.compile(generate(0.5))
        self.is_pass(r, '0.1')
        self.is_pass(r, '.1')
        self.is_pass(r, '-10.12')
        self.is_pass(r, '-.12')
        self.is_pass(r, '1')
        self.is_pass(r, '-10')

    def test_list(self):
        r = re.compile(generate([1]))
        self.assertRaises(ValueError, generate, [])
        self.assertRaises(TypeError, generate, ['a', 1])
        self.is_pass(r, '[]')
        self.is_pass(r, '[1, 2]')
        self.is_fail(r, '["1", "2"]')

    def test_tuple(self):
        r = re.compile(generate((1, 'a', True)))
        self.assertRaises(ValueError, generate, tuple())
        self.is_pass(r, '[, , ]')
        self.is_pass(r, '[100, "abc", false]')
        self.is_pass(r, '[, "abc", false]')
        self.is_pass(r, '[100, , false]')
        self.is_pass(r, '[, , false]')
        self.is_fail(r, '[]')
        self.is_fail(r, '["100", "abc", false]')

    def test_dict(self):
        r = re.compile(generate({'A': 0, 'B': 0.5, 'C': True, 'D': [1], 'E': (2, 'a')}))
        self.assertRaises(ValueError, generate, dict())
        self.is_pass(r, '{"A": 10, "B": -1.23, "C": false, "D": [4,55,   -78], "E": [76, "hello"]}')
        self.is_fail(r, '{"A": "10", "B": -1.23, "C": false, "D": [4,55,   -78], "E": [76, "hello"]}')

    def test_nested(self):
        r = re.compile(generate({'A': (0, ['a']), 'B': {'AA': 'hello', 'BB': [0], 'CC': {'AAA': 0.4}}}))
        self.is_pass(r, '{"A": [-10, []], "B": {"AA": "world", "BB": [ 1 , 2 ], "CC": {"AAA": .333}}}')


if __name__ == '__main__':
    unittest.main()
