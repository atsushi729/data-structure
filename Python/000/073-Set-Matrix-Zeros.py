import unittest


#################### Solution ####################
def set_zeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    zero_index_lists = []
    height = len(matrix)
    width = len(matrix[0])

    # collect zero index position
    for row in range(height):
        for col in range(width):
            if matrix[row][col] == 0:
                zero_index_lists.append([row, col])

    # set zero index position to 0
    for zero_index in zero_index_lists:
        row_index = zero_index[0]
        col_index = zero_index[1]

        # set row to 0
        for col in range(width):
            matrix[row_index][col] = 0

        # set col to 0
        for row in range(height):
            matrix[row][col_index] = 0


def set_zeroes2(matrix: list[list[int]]) -> None:
    ROWS, COLS = len(matrix), len(matrix[0])
    rows, cols = [False] * ROWS, [False] * COLS

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                rows[r] = True
                cols[c] = True

    for r in range(ROWS):
        for c in range(COLS):
            if rows[r] or cols[c]:
                matrix[r][c] = 0


def set_zeroes3(matrix: list[list[int]]) -> None:
    ROWS, COLS = len(matrix), len(matrix[0])
    mark = [[matrix[r][c] for c in range(COLS)] for r in range(ROWS)]

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                for col in range(COLS):
                    mark[r][col] = 0
                for row in range(ROWS):
                    mark[row][c] = 0

    for r in range(ROWS):
        for c in range(COLS):
            matrix[r][c] = mark[r][c]


#################### Test Case ####################
class TestSetZeroes(unittest.TestCase):
    def test_set_zeroes(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        set_zeroes(matrix)
        self.assertEqual(matrix, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        set_zeroes(matrix)
        self.assertEqual(matrix, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])

    def test_set_zeroes2(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        set_zeroes2(matrix)
        self.assertEqual(matrix, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        set_zeroes2(matrix)
        self.assertEqual(matrix, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])

    def test_set_zeroes3(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        set_zeroes3(matrix)
        self.assertEqual(matrix, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        set_zeroes3(matrix)
        self.assertEqual(matrix, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
