# ========================================================================
# Copyright 2022 Emory University
#
# Licensed under the Apache License, Version 2.0 (the `License`);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an `AS IS` BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================

__author__ = 'Jinho D. Choi'

import re
from typing import Dict, Any

from emora_stdm import DialogueFlow


def natex_matching() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`Hello. How are you?`': {  # literal
            'could be better': {  # term
                '`I hope your day gets better soon :(`': 'end'
            },
            '{good, not bad}': {  # set
                '`Glad to hear that you are doing well :)`': 'end'
            },
            '<very, good>': {  # unordered list
                '`So glad that you are having a great day!`': 'end'
            },
            '[so, good]': {  # ordered list (sequence)
                '`Things are just getting better for you!`': 'end'
            },
            '[!hello, world]': {  # rigid sequence
                '`You\'re a programmer!`': 'end'
            },
            '[!-not, aweful]': {  # negation
                '`Sorry to hear that :(`': 'end'
            },
            'error': {
                '`Sorry, I didn\'t understand you.`': 'end'
            }
        }
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    return df


def natex_nesting() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`Hello. How are you?`': {
            '{[{so, very} good], [fantastic]}': {
                '`Things are just getting better for you!`': 'end'
            },
            'error': {
                '`Sorry, I didn\'t understand you.`': 'end'
            }
        }
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    return df


def natex_regex() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`Hello. How are you?`': {
            '[/((?:so|very) good|fantastic)/]': {
                '`Things are just getting better for you!`': 'end'
            },
            'error': {
                '`Sorry, I didn\'t understand you.`': 'end'
            }
        }
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    return df


def regex():
    RE_MR = re.compile(r'M[rs]\.')
    m = RE_MR.match('Dr. Wayne')
    print(m)

    m = RE_MR.match('Mr. Wayne')
    print(m)
    if m:
        print(m.group(), m.start(), m.end())

    print(m.groups())

    RE_MR = re.compile(r'(M[rs])(\.)')
    m = RE_MR.match('Ms. Wayne')
    print(m.groups())
    print(m.group())
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))

    RE_MR = re.compile(r'(M([rs]|rs))(\.)')
    print(RE_MR.match('Mrs. Wayne').groups())
    RE_MR = re.compile(r'(M(?:[rs]|rs))(\.)')
    print(RE_MR.match('Mrs. Wayne').groups())

    s1 = 'Mr. and Ms. Wayne are here'
    s2 = 'Here are Mr. and Mrs. Wayne'

    print(RE_MR.match(s1))
    print(RE_MR.match(s2))

    print(RE_MR.search(s1))
    print(RE_MR.search(s2))

    print(RE_MR.findall(s1))
    print(RE_MR.findall(s2))

    for m in RE_MR.finditer(s1):
        print(m)

    for m in RE_MR.finditer(s2):
        print(m)

    ms = [m for m in RE_MR.finditer(s1)]
    print(ms)

    ms = []
    for m in RE_MR.finditer(s1):
        ms.append(m)


if __name__ == '__main__':
    natex_matching().run()
    # natex_nesting().run()
    # natex_regex().run()
    # regex()
