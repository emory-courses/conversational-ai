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

from typing import List, Tuple, Dict

VALUE_TYPE = bool | str | int | float | list | tuple | dict


def generate(o: VALUE_TYPE) -> str:
    """
    :param o: an object to generate the regular expression for.
    :return: the regular expression for the object.
    :raise ValueError: if the object is not one of ``VALUE_TYPE``.
    """
    match o:
        case bool():
            return r'(?:true|false)'
        case str():
            return r'\".*\"'
        case int():
            return r'-?\d+'
        case float():
            f = r'(?:\.\d+)'
            return r'-?(?:\d+{}?|\d*{})'.format(f, f)
        case list():
            return generate_list(o)
        case tuple():
            return generate_tuple(o)
        case dict():
            return generate_dict(o)
        case _:
            raise TypeError(f'Invalid value type: {type(o)}.')


def generate_list(o: List[VALUE_TYPE]) -> str:
    """
    :param o: a list to generate the regular expression for. All items in the list must have the same type.
    :return: the regular expression for the list.
    :raise ValueError: if the list is empty.
    :raise TypeError: if not all items in the list have the same type.
    """
    if not o: raise ValueError(f'List must not be empty.')
    otype = type(o[0])
    if not all(isinstance(t, otype) for t in o[1:]):
        raise TypeError(f'All items in the list must have the same type: {o}.')
    v = generate(o[0])
    return r'\[(?:\s*{}(?:\s*,\s*{})*)?\s*]'.format(v, v)


def generate_tuple(o: Tuple) -> str:
    """
    :param o: a tuple to generate the regular expression for.
    :return: the regular expression for the tuple.
    :raise ValueError: if the tuple is empty.
    """
    if not o: raise ValueError(f'Tuple must not be empty.')
    ls = [r'\[']
    for i, v in enumerate(o):
        ls.append(r'(?:\s*{})?'.format(generate(v)))
        ls.append(_comma(i, len(o)))
    ls.append(r'\s*]')
    return ''.join(ls)


def generate_dict(o: Dict[str, VALUE_TYPE]) -> str:
    """
    :param o: a dictionary to generate the regular expression for. All keys in the dictionary must be strings.
    :return: the regular expression for the dictionary.
    :raise ValueError: if the dictionary is empty.
    :raise TypeError: if any key in the dictionary is not a string.
    """
    if not o: raise ValueError(f'Dictionary must not be empty.')
    ls = [r'{']
    for i, (k, v) in enumerate(o.items()):
        if not isinstance(k, str): raise TypeError
        key = r'\"{}\"'.format(k)
        ls.append(r'\s*{}\s*:\s*{}'.format(key, generate(v)))
        ls.append(_comma(i, len(o)))
    ls.append(r'\s*}')
    return ''.join(ls)


def _comma(index: int, size: int) -> str:
    """
    :param index: the index of the current item.
    :param size: the size of the collection.
    :return: the regular expressions of a comma for a delimiter in a collection.
    """
    s = r'\s*,'
    return r'(?:{})?'.format(s) if index == size - 1 else s


if __name__ == '__main__':
    s = {"office_location": "White Hall E305", "office_hours": [{"day": "Monday", "begin": "14:00", "end": "15:00"}, {"day": "Friday", "begin": "11:00", "end": "12:30"}]}
    print(generate(s))