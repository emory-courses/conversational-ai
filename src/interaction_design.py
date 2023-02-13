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
from typing import Dict, Any, List

import requests
from emora_stdm import DialogueFlow, Macro, Ngrams


def state_reference() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`What can I do for you?`': {
            '[{time, clock}]': {
                'state': 'time',
                '`It\'s 3PM.`': 'start'
            },
            '[{weather, forecast}]': {
                'state': 'weather',
                '`It\'s sunny outside`': 'start'
            },
            '[play, raining tacos]': {
                'state': 'play_raining_tacos',
                '`It\'s raining tacos. From out of the sky ...`': 'start'
            },
            'error': {
                '`Sorry, I didn\'t understand you.`': 'start'
            },
            '[exit]': {
                'state': 'exit',
                '`Good bye!`': 'end'
            }
        }
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    return df


class MacroWeather(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        terms = ['weather', 'forecast']
        if not any(term for term in terms if term in ngrams):
            return False

        url = 'https://api.weather.gov/gridpoints/FFC/52,88/forecast'
        r = requests.get(url)
        d = json.loads(r.text)
        periods = d['properties']['periods']
        today = periods[0]

        vars['REQUESTED_WEATHER'] = today['detailedForecast']
        return True


def advanced_macro() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`What can I do for you?`': {
            '[{time, clock}]': {
                'state': 'time',
                '`It\'s 3PM.`': 'start'
            },
            '[{weather, forecast}]': {
                'state': 'weather',
                '`It\'s sunny outside`': 'start'
            },
            '[play, raining tacos]': {
                'state': 'play_raining_tacos',
                '`It\'s raining tacos. From out of the sky ...`': 'start'
            },
            'error': {
                '`Sorry, I didn\'t understand you.`': 'start'
            },
            '[exit]': {
                'state': 'exit',
                '`Good bye!`': 'end'
            }
        }
    }

    macros = {
        'WEATHER': MacroWeather(),
        'HELLO': MacroGenerate()
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    df.add_macros(macros)
    return df


def state_reference4() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`Hello. What can I do for you?`': {
            '[{time, clock}]': {
                '`It\'s 3PM.`': 'end'
            },
            '[{weather, forecast}]': {
                '`It\'s sunny outside`': 'end'
            },
            '[play, [!{#LEM(rain), rainy}, #LEM(taco)]]': {
                '`It\'s raining tacos. From out of the sky ...`': 'end'
            },
            'error': {
                '`Sorry, I didn\'t understand you.`': 'end'
            }
        }
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    return df


class MacroGenerate(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        return 'Hello World ' + args[0]


def weather() -> DialogueFlow:
    macros = {
        'WEATHER': MacroWeather(),
        'HELLO': MacroGenerate()
    }

    transitions = {
        'state': 'start',
        '`Hello. What can I do for you?`': {
            '#WEATHER': {
                '$REQUESTED_WEATHER': 'start'
            },
            'error': {
                '#HELLO($REQUESTED_WEATHER)`': 'end'
            }
        }
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    df.add_macros(macros)
    return df


if __name__ == '__main__':
    state_reference().run()
