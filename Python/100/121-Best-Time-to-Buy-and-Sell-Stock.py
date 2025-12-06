import unittest
from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit

    def max_profit_v2(self, prices: List[int]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                res = max(res, sell - buy)
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([7, 1, 5, 3, 6, 4], 5),
            ([7, 6, 4, 3, 1], 0),
            ([1, 2, 3, 4, 5], 4),
            ([3, 2, 6, 5, 0, 3], 4),
        ]

    def test_max_profit(self):
        for prices, expected in self.test_cases:
            with self.subTest(prices=prices, expected=expected):
                self.assertEqual(self.s.max_profit(prices), expected)

    def test_max_profit_v2(self):
        for prices, expected in self.test_cases:
            with self.subTest(prices=prices, expected=expected):
                self.assertEqual(self.s.max_profit_v2(prices), expected)
