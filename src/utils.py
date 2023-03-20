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

import json
import re
from json import JSONDecodeError
from typing import Dict, Any, List, Callable

import openai
from emora_stdm import Macro, Ngrams

from src import regexutils

OPENAI_API_KEY_PATH = 'resources/openai_api.txt'
CHATGPT_MODEL = 'gpt-3.5-turbo'


class MacroGPTJSON(Macro):
    def __init__(self, request: str, full_ex: Dict[str, Any], empty_ex: Dict[str, Any] = None, set_variables: Callable[[Dict[str, Any], Dict[str, Any]], None] = None):
        """
        :param request: the task to be requested regarding the user input (e.g., How does the speaker want to be called?).
        :param full_ex: the example output where all values are filled (e.g., {"call_names": ["Mike", "Michael"]}).
        :param empty_ex: the example output where all collections are empty (e.g., {"call_names": []}).
        :param set_variables: it is a function that takes the STDM variable dictionary and the JSON output dictionary and sets necessary variables.
        """
        self.request = request
        self.full_ex = json.dumps(full_ex)
        self.empty_ex = '' if empty_ex is None else json.dumps(empty_ex)
        self.check = re.compile(regexutils.generate(full_ex))
        self.set_variables = set_variables

    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        examples = f'{self.full_ex} or {self.empty_ex} if unavailable' if self.empty_ex else self.full_ex
        prompt = f'{self.request} Respond in the JSON schema such as {examples}: {ngrams.raw_text().strip()}'
        output = gpt_completion(prompt)
        m = self.check.search(output)
        if not m: return False
        output = m.group().strip()

        try:
            d = json.loads(output)
        except JSONDecodeError:
            print(f'Invalid: {output}')
            return False

        if self.set_variables:
            self.set_variables(vars, d)
        else:
            vars.update(d)
        return True


class MacroNLG(Macro):
    def __init__(self, generate: Callable[[Dict[str, Any]], str]):
        self.generate = generate

    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        return self.generate(vars)


def gpt_completion(input: str) -> str:
    response = openai.ChatCompletion.create(
        model=CHATGPT_MODEL,
        messages=[{'role': 'user', 'content': input}]
    )
    return response['choices'][0]['message']['content'].strip()

# My office is at MSC W302F. My office hours are MW 4-5:30pm