from typing import List
import unittest


class Solution:
    def max_coins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        return dfs(1, len(nums) - 2)

    def max_coins2(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        def dfs(nums):
            if nums == 2:
                return 0
            max_coins = 0
            for i in range(1, len(nums) - 1):
                coins = nums[i - 1] * nums[i] * nums[i + 1]
                new_nums = nums[:i] + nums[i + 1:]
                max_coins = max(max_coins, coins + dfs(new_nums))
            return max_coins

        return dfs(nums)

    def max_coins3(self, nums: List[int]) -> int:
        n = len(nums)
        new_nums = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                for i in range(l, r + 1):
                    coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([3, 1, 5, 8], 167),
            ([1, 5], 10),
            ([4, 2, 3, 7], 143),
            ([1, 2, 3], 12)
        ]

    def test_max_coins(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.max_coins(nums), expected)

    def test_max_coins2(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.max_coins2(nums), expected)

    def test_max_coins3(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.max_coins3(nums), expected)
