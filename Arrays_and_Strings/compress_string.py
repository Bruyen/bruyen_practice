#
# Implement a method to perform a basic string compression using the counts of
# repeated characters. For example, the string 'aabcccccaaa' would become
# 'a2b1c5a3'. If the 'compressed' string would not become smaller than the
# original string, your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a-z).
#
import pytest


def compress_str(string):
    count = 0
    current = string[0]
    new_str = ""

    for char in string:
        if current != char:
            new_str += current
            new_str += str(count)
            current = char
            count = 0
        count += 1
    new_str += char         # For last entry
    new_str += str(count)   # For last entry

    if len(new_str) >= len(string):
        return string

    return new_str


@pytest.mark.parametrize("func,str,expected", [
    (compress_str, 'aabcccccaaa', 'a2b1c5a3'),
    (compress_str, 'aaa', 'a3'),
    (compress_str, 'abcde', 'abcde'),
    (compress_str, 'abababab', 'abababab'),
    (compress_str, 'aaaaaaaaaaaaaaa', 'a15'),
    (compress_str, 'aaaaaaaaaaaaaaabbbbbaaaaaaaaaa', 'a15b5a10'),
    (compress_str, 'cdefcdefcdef', 'cdefcdefcdef'),
    (compress_str, 'aaabbbcccddd', 'a3b3c3d3'),
    (compress_str, 'a', 'a')
])
def test_thingies(func, str, expected):
    assert func(str) == expected
