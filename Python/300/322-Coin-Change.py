from typing import List
import unittest


class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        """
        Time Complexity: O(n*m)
        Space Complexity: O(m)
        """
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

    def coin_change_v2(self, coins: List[int], amount: int) -> int:
        """
        Time Complexity: O(n^m)
        Space Complexity: O(1)
        """

        def dfs(amount):
            if amount == 0:
                return 0

            res = 1e9

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            return res

        min_coins = dfs(amount)
        if min_coins >= 1e9:
            return -1
        return min_coins

    def coin_change_v3(self, coins: List[int], amount: int) -> int:
        """
        Time Complexity: O(n*m)
        Space Complexity: O(m)
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1


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

    def test_coin_change_v2(self):
        self.assertEqual(self.sol.coin_change_v2([1, 2, 5], 11), 3)
        self.assertEqual(self.sol.coin_change_v2([2], 3), -1)
        self.assertEqual(self.sol.coin_change_v2([1], 0), 0)
        self.assertEqual(self.sol.coin_change_v2([1], 1), 1)
        self.assertEqual(self.sol.coin_change_v2([1], 2), 2)

    def test_coin_change_v3(self):
        self.assertEqual(self.sol.coin_change_v3([1, 2, 5], 11), 3)
        self.assertEqual(self.sol.coin_change_v3([2], 3), -1)
        self.assertEqual(self.sol.coin_change_v3([1], 0), 0)
        self.assertEqual(self.sol.coin_change_v3([1], 1), 1)
        self.assertEqual(self.sol.coin_change_v3([1], 2), 2)
