#
# Given an image represented by an NxN matrix, where each pixel in the image is
# 4 bytes, write a method to rotate the image by 90 degrees.
# Can you do this in place?
#
import pytest


# Rotates the matrix in place by rotating one layer at a time.
# Will perform a rotation of 90 degrees clockwise to the corresponding spot
def rotate_matrix(matrix):
    if len(matrix) != len(matrix[0]) or len(matrix) == 0:
        return None

    len_matrix = len(matrix)
    for layer in range(len_matrix // 2):
        first = layer
        last = len_matrix - 1 - layer
        for i in range(first, last):
            offset = i - first
            # Saves the top left most element of layer
            temp = matrix[first][i]
            # top left <- bottom left
            matrix[first][i] = matrix[last - offset][first]
            # bottom left <- bottom right
            matrix[last - offset][first] = matrix[last][last - offset]
            # bottom right <- top right
            matrix[last][last - offset] = matrix[i][last]
            # top right <- top left
            matrix[i][last] = temp

    return matrix


@pytest.mark.parametrize("func, matrix, expected", [
    (rotate_matrix,
        [
            ['a', 'b'],
            ['a', 'b']
        ],
        [
            ['a', 'a'],
            ['b', 'b']
        ]),
    (rotate_matrix,
        [
            ['a', 'b', 'c'],
            ['a', 'b', 'c'],
            ['a', 'b', 'c']
        ],
        [
            ['a', 'a', 'a'],
            ['b', 'b', 'b'],
            ['c', 'c', 'c'],
        ]),
    (rotate_matrix,
        [
            ['a', 'b', 'c', 'd'],
            ['a', 'b', 'c', 'd'],
            ['a', 'b', 'c', 'd'],
            ['a', 'b', 'c', 'd']
        ],
        [
            ['a', 'a', 'a', 'a'],
            ['b', 'b', 'b', 'b'],
            ['c', 'c', 'c', 'c'],
            ['d', 'd', 'd', 'd']
        ]),
    (rotate_matrix,
        [
            ['a', 'a', 'a', 'a'],
            ['b', 'b', 'b', 'b'],
            ['c', 'c', 'c', 'c'],
            ['d', 'd', 'd', 'd']
        ],
        [
            ['d', 'c', 'b', 'a'],
            ['d', 'c', 'b', 'a'],
            ['d', 'c', 'b', 'a'],
            ['d', 'c', 'b', 'a']
        ])
])
def test_thingies(func, matrix, expected):
    result = func(matrix)
    for i in range(len(result)):
        for j in range(len(result[0])):
            assert result[i][j] == expected[i][j]
