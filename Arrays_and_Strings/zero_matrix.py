#
# Write an algorithm such that if an element in an MxN matrix is 0, its
# entire row and column are set to 0.
#
import pytest


def zero_matrix(matrix):
    col_has_zero = False
    row_has_zero = False

    # Determines if there are any zeros in top row and column.
    # Also, use the top row/column as a reference for the rest of the matrix
    for column in matrix:
        if column[0] == 0:
            col_has_zero = True
            break

    for row in matrix[0]:
        if row == 0:
            row_has_zero = True
            break

    # Finds all the zero entries, no need to recheck 1st row/column
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    # Replace entries with 0s, except the references
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    # if the top row/column had 0s at the start, purge row/column
    if col_has_zero:
        for column in matrix:
            column[0] = 0

    if row_has_zero:
        for row in range(0, len(matrix[0])):
            matrix[0][row] = 0

    return matrix


@pytest.mark.parametrize("func, matrix, expected", [
    (zero_matrix,
        [
            [1, 0],
            [1, 2]
        ],
        [
            [0, 0],
            [1, 0]
        ]),
    (zero_matrix,
        [
            [1, 0, 1],
            [1, 1, 1]
        ],
        [
            [0, 0, 0],
            [1, 0, 1]
        ]),
    (zero_matrix,
        [
            [0, 2, 3],
            [1, 2, 3],
            [1, 2, 3]
        ],
        [
            [0, 0, 0],
            [0, 2, 3],
            [0, 2, 3],
        ]),
    (zero_matrix,
        [
            [1, 2, 3],
            [1, 2, 0],
            [1, 2, 3]
        ],
        [
            [1, 2, 0],
            [0, 0, 0],
            [1, 2, 0],
        ]),
    (zero_matrix,
        [
            [1, 2, 3, 4, 5],
            [1, 2, 0, 4, 5],
            [1, 2, 3, 4, 5]
        ],
        [
            [1, 2, 0, 4, 5],
            [0, 0, 0, 0, 0],
            [1, 2, 0, 4, 5],
        ]),
    (zero_matrix,
        [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 0]
        ],
        [
            [1, 2, 3, 4, 0],
            [1, 2, 3, 4, 0],
            [0, 0, 0, 0, 0],
        ]),
    (zero_matrix,
        [
            [0, 2, 3, 4, 5],
            [1, 2, 0, 4, 5],
            [1, 2, 3, 4, 0]
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ])
])
def test_thingies(func, matrix, expected):
    result = func(matrix)
    for i in range(len(result)):
        for j in range(len(result[0])):
            assert result[i][j] == expected[i][j]
