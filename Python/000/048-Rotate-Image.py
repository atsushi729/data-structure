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

    def rotate3(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rotated[j][n - 1 - i] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = rotated[i][j]

    def rotate4(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        if n <= 1:
            return

        # 外側の層から内側へ
        for first in range(n // 2):
            last = n - 1 - first
            # 層の左→右へ走査（四点入れ替えを offset で表現）
            for i in range(first, last):
                offset = i - first

                # 4点スワップ（top ← left ← bottom ← right ← top）
                top = matrix[first][i]  # 退避（上）

                # left -> top
                matrix[first][i] = matrix[last - offset][first]

                # bottom -> left
                matrix[last - offset][first] = matrix[last][last - offset]

                # right -> bottom
                matrix[last][last - offset] = matrix[i][last]

                # top(退避) -> right
                matrix[i][last] = top

    def rotate5(self, matrix: List[List[int]]) -> None:
        rotated = list(map(list, zip(*matrix[::-1])))
        matrix[:] = rotated

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

    def test_rotate3(self):
        for matrix, expected in self.test_cases:
            with self.subTest(matrix=matrix):
                m = deepcopy(matrix)
                self.solution.rotate3(m)
                self.assertEqual(m, expected)

    def test_rotate4(self):
        for matrix, expected in self.test_cases:
            with self.subTest(matrix=matrix):
                m = deepcopy(matrix)
                self.solution.rotate4(m)
                self.assertEqual(m, expected)

    def test_rotate5(self):
        for matrix, expected in self.test_cases:
            with self.subTest(matrix=matrix):
                m = deepcopy(matrix)
                self.solution.rotate5(m)
                self.assertEqual(m, expected)