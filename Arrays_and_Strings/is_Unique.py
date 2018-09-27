#
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
#
import pytest


def is_Uniq(s):
    if not isinstance(s, basestring) or len(s) > 128:
        return False

    count = [0] * 128  # Assuming ASCII values
    for i in s:
        ascii_val = ord(i)
        count[ascii_val] += 1
        if count[ascii_val] > 1:
            return False
    return True


# without an additional data structure
def is_Uniq_v2(s):
    if not isinstance(s, basestring) or len(s) > 128:
        return False

    s = ''.join(sorted(s))  # Assuming O(N log N)

    prev = None
    for i in s:
        if i == prev:
            return False
        prev = i
    return True


@pytest.mark.parametrize("func,stringy,expected", [
    (is_Uniq, 'asdfjkl', True),
    (is_Uniq, 'aaa', False),
    (is_Uniq, 'aba', False),
    (is_Uniq, 'aAbBcC', True),
    (is_Uniq_v2, 'asdfjkl', True),
    (is_Uniq_v2, 'aaa', False),
    (is_Uniq_v2, 'aba', False),
    (is_Uniq_v2, 'aAbBcC', True)
])
def test_thingies(func, stringy, expected):
    assert func(stringy) == expected
