from collections import defaultdict
from typing import List
import unittest


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(i, total):
            if i == len(nums):
                return total == target

            return (backtrack(i + 1, total + nums[i]) +
                    backtrack(i + 1, total - nums[i]))

        return backtrack(0, 0)

    def findTargetSumWays_v2(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(i, total):
            if i == len(nums):
                return total == target
            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                                backtrack(i + 1, total - nums[i]))
            return memo[(i, total)]

        return backtrack(0, 0)

    def findTargetSumWays_v3(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count
        return dp[n][target]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([1, 1, 1, 1, 1], 3, 5),
            ([1], 1, 1),
            ([0, 0, 0], 0, 8),
            ([2, 2, 2, 2, 5], 5, 6),
            ([10], -10, 1),
        ]

    def test_find_target_sum_ways(self):
        for nums, target, expected in self.test_cases:
            self.assertEqual(self.solution.findTargetSumWays(nums, target), expected)

    def test_find_target_sum_ways_v2(self):
        for nums, target, expected in self.test_cases:
            self.assertEqual(self.solution.findTargetSumWays_v2(nums, target), expected)

    def test_find_target_sum_ways_v3(self):
        for nums, target, expected in self.test_cases:
            self.assertEqual(self.solution.findTargetSumWays_v3(nums, target), expected)
