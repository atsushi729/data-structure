from typing import List
import unittest


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0

        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                res += self.matrix[i][j]
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
                self.assertEqual(num_matrix.sumRegion(*query_params), expected)
