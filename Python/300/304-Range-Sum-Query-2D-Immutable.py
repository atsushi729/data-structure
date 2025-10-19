from typing import List
import unittest


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0

        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                res += self.matrix[i][j]
        return res


class NumMatrixV2:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for row in range(len(matrix)):
            self.prefix[row][0] = matrix[row][0]
            for col in range(1, len(matrix[0])):
                self.prefix[row][col] = self.prefix[row][col - 1] + matrix[row][col]

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2 + 1):
            if col1 > 0:
                res += self.prefix[row][col2] - self.prefix[row][col1 - 1]
            else:
                res += self.prefix[row][col2]
        return res


class TestNumMatrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_cases = [
            (
                [[3, 0, 1, 4, 2],
                 [5, 6, 3, 2, 1],
                 [1, 2, 0, 1, 5],
                 [4, 1, 0, 1, 7],
                 [1, 0, 3, 0, 5]],
                (2, 1, 4, 3),
                8
            ),
            (
                [[3, 0, 1, 4, 2],
                 [5, 6, 3, 2, 1],
                 [1, 2, 0, 1, 5],
                 [4, 1, 0, 1, 7],
                 [1, 0, 3, 0, 5]],
                (1, 1, 2, 2),
                11
            ),
            (
                [[3, 0, 1, 4, 2],
                 [5, 6, 3, 2, 1],
                 [1, 2, 0, 1, 5],
                 [4, 1, 0, 1, 7],
                 [1, 0, 3, 0, 5]],
                (1, 2, 2, 4),
                12
            ),
        ]

    def test_sumRegion(self):
        for matrix_data, query_params, expected in self.test_cases:
            with self.subTest(matrix_data=matrix_data,
                              query_params=query_params,
                              expected=expected):
                num_matrix = NumMatrix(matrix_data)
                self.assertEqual(num_matrix.sum_region(*query_params), expected)

    def test_sumRegion_v2(self):
        for matrix_data, query_params, expected in self.test_cases:
            with self.subTest(matrix_data=matrix_data,
                              query_params=query_params,
                              expected=expected):
                num_matrix = NumMatrixV2(matrix_data)
                self.assertEqual(num_matrix.sum_region(*query_params), expected)