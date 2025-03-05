from typing import List
import unittest


class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            res = 1e9

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res
            return res

        min_coins = dfs(amount)
        return -1 if min_coins >= 1e9 else min_coins

#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_coin_change(self):
        self.assertEqual(self.sol.coin_change([1, 2, 5], 11), 3)
        self.assertEqual(self.sol.coin_change([2], 3), -1)
        self.assertEqual(self.sol.coin_change([1], 0), 0)
        self.assertEqual(self.sol.coin_change([1], 1), 1)
        self.assertEqual(self.sol.coin_change([1], 2), 2)