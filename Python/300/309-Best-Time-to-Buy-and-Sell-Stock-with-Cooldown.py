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

    def max_profit_v2(self, prices: List[int]) -> int:
        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)

    def max_profit_v3(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = dp[i + 1][False] - prices[i] if i + 1 < n else -prices[i]
                    cooldown = dp[i + 1][True] if i + 1 < n else 0
                    dp[i][1] = max(buy, cooldown)
                else:
                    sell = dp[i + 2][True] + prices[i] if i + 2 < n else prices[i]
                    cooldown = dp[i + 1][False] if i + 1 < n else 0
                    dp[i][0] = max(sell, cooldown)

        return dp[0][1]

    def max_profit_v4(self, prices: List[int]) -> int:
        n = len(prices)
        dp1_buy, dp1_sell = 0, 0
        dp2_buy = 0

        for i in range(n - 1, -1, -1):
            dp_buy = max(dp1_sell - prices[i], dp1_buy)
            dp_sell = max(dp2_buy + prices[i], dp1_sell)
            dp2_buy = dp1_buy
            dp1_buy, dp1_sell = dp_buy, dp_sell

        return dp1_buy


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

    def test_max_profit_v2(self):
        self.assertEqual(self.solution.max_profit_v2([1, 2, 3, 0, 2]), 3)
        self.assertEqual(self.solution.max_profit_v2([1]), 0)
        self.assertEqual(self.solution.max_profit_v2([1, 2]), 1)
        self.assertEqual(self.solution.max_profit_v2([2, 1]), 0)
        self.assertEqual(self.solution.max_profit_v2([1, 2, 3]), 2)

    def test_max_profit_v3(self):
        self.assertEqual(self.solution.max_profit_v3([1, 2, 3, 0, 2]), 3)
        self.assertEqual(self.solution.max_profit_v3([1]), 0)
        self.assertEqual(self.solution.max_profit_v3([1, 2]), 1)
        self.assertEqual(self.solution.max_profit_v3([2, 1]), 0)
        self.assertEqual(self.solution.max_profit_v3([1, 2, 3]), 2)

    def test_max_profit_v4(self):
        self.assertEqual(self.solution.max_profit_v4([1, 2, 3, 0, 2]), 3)
        self.assertEqual(self.solution.max_profit_v4([1]), 0)
        self.assertEqual(self.solution.max_profit_v4([1, 2]), 1)
        self.assertEqual(self.solution.max_profit_v4([2, 1]), 0)
        self.assertEqual(self.solution.max_profit_v4([1, 2, 3]), 2)
