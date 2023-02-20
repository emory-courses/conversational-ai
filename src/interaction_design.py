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
import time
from typing import Dict, Any, List

import requests
import vlc
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


def advanced_interaction() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`What can I do for you?`': {
            '[play, [!{#LEM(rain), rainy}, #LEM(taco)]]': {
                'state': 'play_raining_tacos',
                '#IF($RAINING_TACOS) `Don\'t make me sing this again!`': 'start',
                '#IF(#PLAY_RAINING_TACOS) `It\'s raining tacos. From out of the sky ...` #SETBOOL(RAINING_TACOS, True)': 'start',
            },
            '[{time, clock}]': {
                'state': 'time',
                '#TIME': 'end'
            },
            '[{weather, forecast}]': {
                'state': 'weather',
                '#WEATHER': 'end'
            },
            '#UNX': {
                '`Thanks for sharing.`': 'start'
            },
        }
    }

    macros = {
        'SETBOOL': MacroSetBool(),
        'PLAY_RAINING_TACOS': MacroPlayRainingTacos(),
        'TIME': MacroTime(),
        'WEATHER': MacroWeather()
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    df.add_macros(macros)
    return df


class MacroSetBool(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[str]):
        if len(args) != 2:
            return False

        variable = args[0]
        if variable[0] == '$':
            variable = variable[1:]

        boolean = args[1].lower()
        if boolean not in {'true', 'false'}:
            return False

        vars[variable] = bool(boolean)
        return True


class MacroPlayRainingTacos(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[str]):
        if not vars.get('RAINING_TACOS', False):
            vlc.MediaPlayer("resources/raining_tacos.mp3").play()
            return True
        return False


class MacroTime(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[str]):
        current_time = time.strftime('%H:%M')
        return "It's currently {}.".format(current_time)


class MacroWeather(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        url = 'https://api.weather.gov/gridpoints/FFC/52,88/forecast'
        r = requests.get(url)
        d = json.loads(r.text)
        periods = d['properties']['periods']
        today = periods[0]
        return today['detailedForecast']


def compound_states() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '#GATE `Let\'s talk about music.`': 'music',
        '#GATE `Let\'s talk about movies.`': 'movie',
        '`That\'s all I can talk about.`': {
            'state': 'end',
            'score': 0.1
        }
    }

    transitions_music = {
        'state': 'music',
        '`What is your favorite song?`': {
            '[[!{#LEM(rain), rainy}, #LEM(taco)]]': {
                '`I love children\'s songs by Parry Gripp.`': 'start',
            },
            'error': {
                '`Sorry, I don\'t know that song.`': 'movie'
            }
        }
    }

    transitions_movie = {
        'state': 'movie',
        '`What is your favorite movie?`': {
            '[{#LEM(avenger), iron man, hulk}]': {
                '`I love the Marvel Cinematic Universe.`': 'start',
            },
            'error': {
                '`Sorry, I don\'t know that movie.`': 'music'
            }
        }
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    df.load_transitions(transitions_music)
    df.load_transitions(transitions_movie)
    return df


def global_transition() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`Hi there, how are you doing today?`': {
            '[{good, fantastic}]': {
                'state': 'good',
                '`Glad to hear that.` #WHAT_ELSE': {
                    '[#LEM(movie)]': 'movie',
                    '[music]': 'music',
                    'error': {
                        'state': 'goodbye',
                        '`Goodbye!`': 'end'
                    }
                }
            },
            'error': 'goodbye'
        }
    }

    music_transitions = {
        'state': 'music',
        '`My favorite song is "Raining Tacos"! What\'s yours?`': {
            'error': 'good'
        }
    }

    movie_transitions = {
        'state': 'movie',
        '`My favorite movie is "Spider-Man: Homecoming"! What\'s yours?`': {
            'error': 'good'
        }
    }

    macros = {
        'WHAT_ELSE': MacroWhatElse()
    }

    gloabl_transitions = {
        '[{covid, corona, virus}]': {
            'score': 0.5,
            '`I hope you are OK.`': 'good'
        },
        '[{birthday}]': {
            'score': 0.5,
            '`Happy birthday to you!`': 'good'
        }
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    df.load_transitions(music_transitions)
    df.load_transitions(movie_transitions)
    df.add_macros(macros)
    df.load_global_nlu(gloabl_transitions)
    return df


class MacroWhatElse(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        vn = 'HAVE_TALK'
        if vn in vars and vars[vn]:
            return 'What else do you want to talk about?'
        else:
            vars[vn] = True
            return 'What do you want to talk about?'


if __name__ == '__main__':
    # state_reference().run()
    # advanced_interaction().run()
    # compound_states().run()
    global_transition().run()
