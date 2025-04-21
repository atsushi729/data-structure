from typing import List
import unittest


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Time complexity: O(2^n)
        Space complexity: O(n)
        """
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

    def change_v2(self, amount: int, coins: List[int]) -> int:
        """
        Time complexity: O(n * amount)
        Space complexity: O(n * amount)
        """
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

        def dfs(i, a):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            if memo[i][a] != -1:
                return memo[i][a]

            res = 0
            if a >= coins[i]:
                res = dfs(i + 1, a)
                res += dfs(i, a - coins[i])

            memo[i][a] = res
            return res

        return dfs(0, amount)

    def change_v3(self, amount: int, coins: List[int]) -> int:
        """
        Time complexity: O(n * amount)
        Space complexity: O(n * amount)
        """
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a]
                    dp[i][a] += dp[i][a - coins[i]]

        return dp[0][amount]

    def change_v4(self, amount: int, coins: List[int]) -> int:
        """
        Time complexity: O(n * amount)
        Space complexity: O(amount)
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[amount]

    def change_v5(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            (5, [1, 2, 5], 4),
            (3, [2], 0),
            (10, [10], 1),
            (0, [1], 1),
            (7, [2, 3, 6], 1),
        ]

    def test_change(self):
        for amount, coins, expected in self.test_cases:
            self.assertEqual(self.solution.change(amount, coins), expected)

    def test_change_v2(self):
        for amount, coins, expected in self.test_cases:
            self.assertEqual(self.solution.change_v2(amount, coins), expected)

    def test_change_v3(self):
        for amount, coins, expected in self.test_cases:
            self.assertEqual(self.solution.change_v3(amount, coins), expected)

    def test_change_v4(self):
        for amount, coins, expected in self.test_cases:
            self.assertEqual(self.solution.change_v4(amount, coins), expected)

    def test_change_v5(self):
        for amount, coins, expected in self.test_cases:
            self.assertEqual(self.solution.change_v5(amount, coins), expected)
