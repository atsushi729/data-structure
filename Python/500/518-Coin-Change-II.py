from typing import List
import unittest


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        def dfs(i, a):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0

            res = 0
            if a >= coins[i]:
                res = dfs(i + 1, a)
                res += dfs(i, a - coins[i])
            return res

        return dfs(0, amount)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            (5, [1, 2, 5], 4),
            (3, [2], 0),
            (10, [10], 1),
            (0, [1], 1),
            (7, [2, 3, 6], 8),
        ]

    def test_change(self):
        for amount, coins, expected in self.test_cases:
            self.assertEqual(self.solution.change(amount, coins), expected)
