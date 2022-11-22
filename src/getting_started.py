# ========================================================================
# Copyright 2022 Emory University
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

from emora_stdm import DialogueFlow


def chatbot0() -> DialogueFlow:
    chatbot = DialogueFlow('start', end_state='end')

    chatbot.add_system_transition('start', 's1', '"Hello. How are you?"')
    chatbot.add_user_transition('s1', 'u1', '[{fine, good, fantastic}]')
    chatbot.add_system_transition('u1', 's2', '"Glad to hear that you are doing well :)"')
    chatbot.set_error_successor('s2', 'e1')
    chatbot.add_system_transition('e1', 'end', '"See you later!"')
    chatbot.set_error_successor('s1', 'e2')
    chatbot.add_system_transition('e2', 's3', '"I hope your day gets better soon :("')
    chatbot.set_error_successor('s3', 'e3')
    chatbot.add_system_transition('e3', 'end', '"Take care!"')

    return chatbot


def chatbot1() -> DialogueFlow:
    chatbot = DialogueFlow('start', end_state='end')

    transitions = {
        'state': 'start',
        '"Hello. How are you?"': {
            '[{fine, good, fantastic}]': {
                '"Glad to hear that you are doing well :)"': {
                    'error': {
                        '"See you later!"': 'end'
                    }
                }
            },
            'error': {
                '"I hope your day gets better soon :("': {
                    'error': {
                        '"Take care!"': 'end'
                    }
                }
            }
        }
    }

    chatbot.load_transitions(transitions)
    return chatbot


if __name__ == '__main__':
    chatbot0().run()
    chatbot1().run()
