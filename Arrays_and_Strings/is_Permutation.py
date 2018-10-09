#
# Given two strings, write a method to decide if one is a permutation
# of the other.
#
import pytest


# Assuming case sensitive and whitespace significant

# This solution fails as there are strings that may have different
# characters but their ascii values add up to the same total.
# EX: 'a' + 'a' + 'a' = 291 = '[' + 'd' + 'd'
#
# def is_permutation(str1, str2):
#     if len(str1) != len(str2):
#         return False
#
#     sums = {'sum1': 0, 'sum2': 0}
#
#     for char in str1:
#         sums['sum1'] += ord(char)
#
#     for char in str2:
#         sums['sum2'] += ord(char)
#
#     if sums['sum1'] == sums['sum2']:
#         return True
#
#     return False


# 2nd Try
# Another solution may be to sort the strings and compare their values.
# However, sorting may have a longer run time.
def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    table = [0] * 128  # Assuming ASCII values

    for char in str1:
        table[ord(char)] += 1

    for char in str2:
        value = ord(char)
        table[value] -= 1
        if table[value] < 0:
            return False

    return True


@pytest.mark.parametrize("func,str1,str2,expected", [
    (is_permutation, 'abc', 'cba', True),
    (is_permutation, 'abc', 'abc', True),
    (is_permutation, 'abc', 'bca', True),
    (is_permutation, 'abc', 'abh', False),
    (is_permutation, 'abc', 'abcd', False),
    (is_permutation, 'abc', 'abb', False),
    (is_permutation, 'aaa', '[dd', False)
])
def test_thingies(func, str1, str2, expected):
    assert func(str1, str2) == expected
