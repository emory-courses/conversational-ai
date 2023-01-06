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


def state_transition() -> Dict[str, Any]:
    return {
        'state': 'start',
        '`Hello. How are you?`': {
            'good': {
                '`Glad to hear that you are doing well :)`': 'end'
            },
            'bad': {
                '`I hope your day gets better soon :(`': 'end'
            },
            'error': {
                '`Sorry, I didn\'t understand you.`': 'end'
            }
        }
    }


def matching_strategy() -> Dict[str, Any]:
    return {
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


def multiturn_dialogue() -> Dict[str, Any]:
    return {
        'state': 'start',
        '`Hello. How are you?`': {
            '[{good, fantastic}]': {
                '`Glad to hear that you are doing well :)`': {
                    '[{how, and}, {you, going}]': {
                        '`I feel superb. Thank you!`': 'end'
                    },
                    'error': {
                        '`You are the best!`': 'end'
                    }
                }
            },
            'error': {
                '`Got it; thanks for sharing.`': 'end'
            },
        }
    }


df = DialogueFlow('start', end_state='end')
# df.load_transitions(state_transitions())
# df.load_transitions(matching_strategies())
df.load_transitions(multiturn_dialogue())

if __name__ == '__main__':
    df.run()
