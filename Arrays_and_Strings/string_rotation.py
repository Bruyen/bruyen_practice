#
# Assume you have a method isSubstring which checks if one word is a substring
# of another. Given 2 strings, s1 and s2, write code to check if s2 is a
# rotation ofk s1 using only one call to isSubstring.
#
# EX:
# "waterbottle" is a rotation of "erbottlewat"
#
import pytest


def isSubstring(s1, s2):
    return s1 in s2


def is_str_rotate(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 != len2 or len1 < 0:
        return False

    return isSubstring(s1, s2+s2)


@pytest.mark.parametrize("func, s1, s2, expected", [
    (is_str_rotate, "waterbottle", "erbottlewat", True),
    (is_str_rotate, "airbubble", "bubbleair", True),
    (is_str_rotate, "xyz", "yzx", True),
    (is_str_rotate, "waterbottle", "erbottlewata", False),
    (is_str_rotate, "waterbottleb", "erbottlewat", False),
    (is_str_rotate, "", "erbottlewat", False)
])
def test_thingies(func, s1, s2, expected):
    assert func(s1, s2) == expected
