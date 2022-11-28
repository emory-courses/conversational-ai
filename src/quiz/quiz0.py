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

df = DialogueFlow('start')
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

df.load_transitions(transitions)
df.run()
