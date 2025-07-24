from typing import List
import unittest


class Solution:
    def longest_increasing_path(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, prev_val):
            if (r < 0 or c < 0 or r == rows or c == cols or matrix[r][c] <= prev_val):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            dp[(r, c)] = res
            return res

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, -1)

        return max(dp.values())


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
            ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
            ([[1]], 1),
            ([[7, 8, 9], [6, 5, 10], [5, 4, 11]], 8)
        ]

    def test_longest_increasing_path(self):
        for matrix, expected in self.test_cases:
            with self.subTest(matrix=matrix):
                result = self.solution.longest_increasing_path(matrix)
                self.assertEqual(result, expected)
