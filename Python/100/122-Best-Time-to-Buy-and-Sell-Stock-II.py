from typing import List
import unittest


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    def max_profit_v2(self, prices: List[int]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n)
        """

        def rec(i, bought):
            if i == len(prices):
                return 0

            res = rec(i + 1, bought)
            if bought:
                res = max(res, prices[i] + rec(i + 1, False))
            else:
                res = max(res, -prices[i] + rec(i + 1, True))
            return res

        return rec(0, False)

    def max_profit_v3(self, prices: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            dp[i][0] = max(dp[i + 1][0], -prices[i] + dp[i + 1][1])
            dp[i][1] = max(dp[i + 1][1], prices[i] + dp[i + 1][0])
        return dp[0][0]

    def max_profit_v4(self, prices: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        dp = {}

        def rec(i, bought):
            if i == len(prices):
                return 0
            if (i, bought) in dp:
                return dp[(i, bought)]

            res = rec(i + 1, bought)

            if bought:
                res = max(res, prices[i] + rec(i + 1, False))
            else:
                res = max(res, -prices[i] + rec(i + 1, True))

            dp[(i, bought)] = res
            return res

        return rec(0, False)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            ([7, 1, 5, 3, 6, 4], 7),
            ([1, 2, 3, 4, 5], 4),
            ([7, 6, 4, 3, 1], 0),
            ([3, 2, 6, 5, 0, 3], 7),
            ([1], 0),
            ([1, 2], 1),
            ([2, 1], 0),
            ([1, 2, 3], 2),
            ([3, 2, 1], 0),
        ]

    def test_max_profit(self):
        for prices, expected in self.test_cases:
            with self.subTest(prices=prices, expected=expected):
                self.assertEqual(self.s.max_profit(prices), expected)

    def test_max_profit_v2(self):
        for prices, expected in self.test_cases:
            with self.subTest(prices=prices, expected=expected):
                self.assertEqual(self.s.max_profit_v2(prices), expected)

    def test_max_profit_v3(self):
        for prices, expected in self.test_cases:
            with self.subTest(prices=prices, expected=expected):
                self.assertEqual(self.s.max_profit_v3(prices), expected)

    def test_max_profit_v4(self):
        for prices, expected in self.test_cases:
            with self.subTest(prices=prices, expected=expected):
                self.assertEqual(self.s.max_profit_v4(prices), expected)
