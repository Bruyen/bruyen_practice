#
# Given a string, write a function to check if it is a permutation of a
# palindrome. A palindrome is a word of phrase that is the same forwards
# and backwards. A permutation is a rearragement of letters.
# The palindrome does not need to be limited to dictionary words.
#
# EX:
# Input:  'Tact Coa'
# Output: 'True' (Permutations are: 'taco cat', 'atco cta', 'ctao atc')
#

import pytest


#
# Since this problem defines palindromes as words and phrases, I will
# confine myself to using only alphabetical characters. I will ignore other
# characters such as spaces, tabs, and punctuation.
#
# Another observation is that I need not enumerate nor construct any
# permutations. I simply only need to identify whether a permutation
# of a palindrome exists.
#
def is_palindrome_permutation(string):

    count = [0] * 26
    for char in string.lower():
        char_val = ord(char)
        # Between a and z on ASCII table
        if (char_val >= 97 and char_val <= 122):
            count[char_val-97] += 1

    # If there is an even number of a character, we can create a palindrome
    # If there is more than one character that has an odd amount, then we can
    # not create a palindrome.
    num_odds = 0

    for value in count:
        if num_odds > 1:
            return False
        if value % 2 != 0:
            num_odds += 1

    return True


@pytest.mark.parametrize("func,string,expected", [
    (is_palindrome_permutation, 'Tact Coa', True),
    (is_palindrome_permutation, 'race car', True),
    (is_palindrome_permutation, 'abcdefg', False),
    (is_palindrome_permutation, 'race cat', False),
    (is_palindrome_permutation, 'tactcoapapa', True)
])
def test_thingies(func, string, expected):
    assert func(string) == expected
