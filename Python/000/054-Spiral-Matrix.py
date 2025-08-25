from typing import List
import unittest


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []

        # append all the elements in the given direction
        def dfs(row, col, r, c, dr, dc):
            if row == 0 or col == 0:
                return

            for i in range(col):
                r += dr
                c += dc
                res.append(matrix[r][c])

            # sub-problem
            dfs(col, row - 1, r, c, dc, -dr)

        # start by going to the right
        dfs(m, n, 0, -1, 0, 1)
        return res

    def spiralOrder3(self, matrix: List[List[int]]) -> List[int]:
        res = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = [len(matrix[0]), len(matrix) - 1]

        r, c, d = 0, -1, 0
        while steps[d & 1]:
            for i in range(steps[d & 1]):
                r += directions[d][0]
                c += directions[d][1]
                res.append(matrix[r][c])
            steps[d & 1] -= 1
            d += 1
            d %= 4
        return res

class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()
        cls.test_cases = [
            (
                [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]],
                [1, 2, 3, 6, 9, 8, 7, 4, 5]
            ),
            (
                [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]],
                [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
            ),
            (
                [[1]],
                [1]
            ),
            (
                [[1], [2], [3], [4]],
                [1, 2, 3, 4]
            ),
            (
                [[1, 2, 3, 4]],
                [1, 2, 3, 4]
            ),
        ]

    def test_spiralOrder(self):
        for matrix, expected in self.test_cases:
            with self.subTest(matrix=matrix):
                result = self.sol.spiralOrder(matrix)
                self.assertEqual(result, expected)

    def test_spiralOrder2(self):
        for matrix, expected in self.test_cases:
            with self.subTest(matrix=matrix):
                result = self.sol.spiralOrder2(matrix)
                self.assertEqual(result, expected)

    def test_spiralOrder3(self):
        for matrix, expected in self.test_cases:
            with self.subTest(matrix=matrix):
                result = self.sol.spiralOrder3(matrix)
                self.assertEqual(result, expected)