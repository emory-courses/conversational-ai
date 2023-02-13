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
from typing import Dict, Any, List

from emora_stdm import DialogueFlow, Macro, Ngrams


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


def natex_variable() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`What is your favorite animal?`': {
            '[$FAVORITE_ANIMAL={dogs, cats, hamsters}]': {
                '`I like` $FAVORITE_ANIMAL `too!`': 'end'
            },
            'error': {
                '`I\'ve never heard of that animal.`': 'end'
            }
        }
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    return df


def natex_ontology1() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`What is your favorite animal?`': {
            '[{dog, ape, rat}]': {
                '`I love mammals!`': 'end'
            },
            '[{snake, lizard}]': {
                '`Reptiles are slick, haha`': 'end'
            },
            '[{frog, salamander}]': {
                '`Amphibians can be cute :)`': 'end'
            },
            'error': {
                '`I\'ve never heard of that animal.`': 'end'
            }
        }
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    return df


def natex_ontology2() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`What is your favorite animal?`': {
            '[#ONT(mammal)]': {
                '`I love mammals!`': 'end'
            },
            '[#ONT(reptile)]': {
                '`Reptiles are slick, haha`': 'end'
            },
            '[#ONT(amphibian)]': {
                '`Amphibians can be cute :)`': 'end'
            },
            'error': {
                '`I\'ve never heard of that animal.`': 'end'
            }
        }
    }

    df = DialogueFlow('start', end_state='end')
    df.knowledge_base().load_json_file('resources/ontology_animal.json')
    df.load_transitions(transitions)
    return df


def natex_ontology3() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`What is your favorite animal?`': {
            '[$FAVORITE_ANIMAL=#ONT(mammal)]': {
                '`I love` $FAVORITE_ANIMAL `!`': 'end'
            },
            '[$FAVORITE_ANIMAL=#ONT(reptile)]': {
                '$FAVORITE_ANIMAL `are slick, haha`': 'end'
            },
            '[$FAVORITE_ANIMAL=#ONT(amphibian)]': {
                '$FAVORITE_ANIMAL `can be cute :)`': 'end'
            },
            'error': {
                '`I\'ve never heard of that animal.`': 'end'
            }
        }
    }

    df = DialogueFlow('start', end_state='end')
    df.knowledge_base().load_json_file('resources/ontology_animal.json')
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


def regex_natex() -> DialogueFlow:
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


def regex_natex_variable() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`Hello. What should I call you?`': {
            '[/(?<FIRSTNAME>[a-z]+) (?<LASTNAME>[a-z]+)/]': {
                '`It\'s nice to meet you,` $FIRSTNAME `. I know several other` $LASTNAME `.`': 'end'
            },
            'error': {
                '`Sorry, I didn\'t understand you.`': 'end'
            }
        }
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    return df


class MacroGetName(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        r = re.compile(r"(mr|mrs|ms|dr)?(?:^|\s)([a-z']+)(?:\s([a-z']+))?")
        m = r.search(ngrams.text())
        if m is None: return False

        title, firstname, lastname = None, None, None

        if m.group(1):
            title = m.group(1)
            if m.group(3):
                firstname = m.group(2)
                lastname = m.group(3)
            else:
                firstname = m.group()
                lastname = m.group(2)
        else:
            firstname = m.group(2)
            lastname = m.group(3)

        vars['TITLE'] = title
        vars['FIRSTNAME'] = firstname
        vars['LASTNAME'] = lastname

        return True


def macro() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`Hello. What should I call you?`': {
            '#GET_NAME': {
                '`It\'s nice to meet you,` $FIRSTNAME `.` $LASTNAME `is my favorite name.`': 'end'
            },
            'error': {
                '`Sorry, I didn\'t understand you.`': 'end'
            }
        }
    }

    macros = {
        'GET_NAME': MacroGetName()
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    df.add_macros(macros)
    return df


if __name__ == '__main__':
    natex_matching().run()
    # natex_nesting().run()
    # natex_variable().run()
    # natex_ontology1().run()
    # natex_ontology2().run()
    # natex_ontology3().run()
    # regex()
    # regex_natex().run()
    # regex_natex_variable().run()
    # macro().run()
