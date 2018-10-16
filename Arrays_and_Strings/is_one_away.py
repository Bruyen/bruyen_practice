#
# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit
# or zero edits away.
#
# EX:
# pale,  ple   -> True
# pales, pale  -> True
# pale,  bale, -> True
# pale,  bake, -> False
#
import pytest


def is_one_away(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    s1 = 0
    s2 = 0
    is_different = False

    while s1 < len(str1) and s2 < len(str2):
        if(str1[s1] != str2[s2]):
            if(is_different):
                return False
            is_different = True

            if(len(str1) > len(str2)):
                s1 += 1
            elif (len(str1) < len(str2)):
                s2 += 1

        s1 += 1
        s2 += 1
    return True


@pytest.mark.parametrize("func,str1,str2,expected", [
    (is_one_away, 'pale', 'ple', True),
    (is_one_away, 'pales', 'pale', True),
    (is_one_away, 'pale', 'bale', True),
    (is_one_away, 'pale', 'bake', False),
    (is_one_away, 'bear', 'beer', True),
    (is_one_away, 'woop', 'oop', True),
    (is_one_away, 'thingies', 'thing', False),
    (is_one_away, 'pale', 'pale', True)
])
def test_thingies(func, str1, str2, expected):
    assert func(str1, str2) == expected
