import unittest


#################### Solution ####################
def is_toeplitz_matrix(matrix: list[list[int]]) -> bool:
    if not matrix:
        return False

    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
    return True


def is_toeplitz_matrix_v2(matrix: list[list[int]]) -> bool:
    rows, cols = len(matrix), len(matrix[0])

    if rows == 1 or cols == 1:
        return True

    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
    return True


#################### Test Case ####################
class TestIsToeplitzMatrix(unittest.TestCase):
    def test_is_toeplitz_matrix(self):
        self.assertEqual(is_toeplitz_matrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]), True)
        self.assertEqual(is_toeplitz_matrix([[1, 2], [2, 2]]), False)

    def test_is_toeplitz_matrix_v2(self):
        self.assertEqual(is_toeplitz_matrix_v2([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]), True)
        self.assertEqual(is_toeplitz_matrix_v2([[1, 2], [2, 2]]), False)
