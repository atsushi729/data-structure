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
