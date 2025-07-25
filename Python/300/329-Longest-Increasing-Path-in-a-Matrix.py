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

    def longest_increasing_path2(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c, prevVal):
            if (min(r, c) < 0 or r >= ROWS or
                    c >= COLS or matrix[r][c] <= prevVal
            ):
                return 0

            res = 1
            for d in directions:
                res = max(res, 1 + dfs(r + d[0], c + d[1], matrix[r][c]))
            return res

        LIP = 0
        for r in range(ROWS):
            for c in range(COLS):
                LIP = max(LIP, dfs(r, c, float('-inf')))
        return LIP


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

    def test_longest_increasing_path2(self):
        for matrix, expected in self.test_cases:
            with self.subTest(matrix=matrix):
                result = self.solution.longest_increasing_path2(matrix)
                self.assertEqual(result, expected)
