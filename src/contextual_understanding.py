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

from typing import Dict, Any

from emora_stdm import DialogueFlow




def literal() -> Dict[str, Any]:
    transitions = {
        'state': 'start',
        '`Hello. How are you?`': {
            '[{good, fantastic}]': {
                '`Glad to hear that you are doing well :)`': 'end'
            },
            '[{bad, could be better}]': {
                '`I hope your day gets better soon :(`': 'end'
            },
            '[{how, and}, {you, going}]': {
                '`I feel superb. Thank you!`': 'end'
            },
            'error': {
                '`Sorry, I didn\'t understand you.`': 'end'
            },
        }
    }

    return transitions


transitions = {
    'state': 'start',
    '`Hello. How are you?`': {      # literal
        'could be better': {        # string
            '`I hope your day gets better soon :(`': 'end'
        },
        '{good, not bad}': {        # set
            '`Glad to hear that you are doing well :)`': 'end'
        },
        '<very, good>': {           # unordered list
            '`So glad that you are having a great day!`': 'end'
        },
        '[so, good]': {             # ordered list (sequence)
            '`Things are just getting better for you!`': 'end'
        },
        '/(fantastic|terrific)/': {             # ordered list (sequence)
            '`Nothing like an awesome day!`': 'end'
        },
        'error': {
            '`Sorry, I didn\'t understand you.`': 'end'
        }
    }
}

df = DialogueFlow('start', end_state='end')
df.load_transitions(transitions)

if __name__ == '__main__':
    df.run()
