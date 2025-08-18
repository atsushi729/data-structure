from typing import List
import unittest
from copy import deepcopy


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                top_left = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = top_left
            r -= 1
            l += 1

    def rotate2(self, matrix: List[List[int]]) -> None:
        # Reverse the matrix vertically
        matrix.reverse()
        # Transpose the matrix
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
            ([[5]], [[5]]),
            ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
            ([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]],
             [[13, 9, 5, 1],
              [14, 10, 6, 2],
              [15, 11, 7, 3],
              [16, 12, 8, 4]])
        ]

    def test_rotate(self):
        for matrix, expected in self.test_cases:
            with self.subTest(matrix=matrix):
                m = deepcopy(matrix)
                self.solution.rotate(m)
                self.assertEqual(m, expected)

    def test_rotate2(self):
        for matrix, expected in self.test_cases:
            with self.subTest(matrix=matrix):
                m = deepcopy(matrix)
                self.solution.rotate2(m)
                self.assertEqual(m, expected)
