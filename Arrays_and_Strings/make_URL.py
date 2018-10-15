#
# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold
# additional characters, and that you are given the "true" length of the
# string.
#
# EX: Input:  "Mr John Smith    ", length is 13
#     Output: "Mr%20John%20Smith"
#
import pytest


def url_ify(string, len):
    if ' ' not in string:
        return -1

    new_string = ""
    for i in range(len):
        if string[i] == ' ':
            new_string += '%20'
        else:
            new_string += string[i]

    return new_string


@pytest.mark.parametrize("func,string,len,expected", [
    (url_ify, 'Mr John Smith    ', 13, 'Mr%20John%20Smith'),
    (url_ify, '     Mr John Smith                     ', 18, '%20%20%20%20%20Mr%20John%20Smith'),
    (url_ify, 'Mr   John   Smith', 17, 'Mr%20%20%20John%20%20%20Smith'),
])
def test_thingies(func, string, len, expected):
    assert func(string, len) == expected
