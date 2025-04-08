from typing import List
import unittest


class Solution:
    def max_profit(self, prices: List[int]) -> int:

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                return max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                return max(sell, cooldown)

        return dfs(0, True)


class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_max_profit(self):
        self.assertEqual(self.solution.max_profit([1, 2, 3, 0, 2]), 3)
        self.assertEqual(self.solution.max_profit([1]), 0)
        self.assertEqual(self.solution.max_profit([1, 2]), 1)
        self.assertEqual(self.solution.max_profit([2, 1]), 0)
        self.assertEqual(self.solution.max_profit([1, 2, 3]), 2)
