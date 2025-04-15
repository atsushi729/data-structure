from typing import List
import unittest


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]

        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                res = max(res, cur)
        return res

    def max_sub_array_v2(self, nums: List[int]) -> int:
        memo = [[None] * 2 for _ in range(len(nums) + 1)]

        def dfs(i, flag):
            if i == len(nums):
                return 0 if flag else -1e6
            if memo[i][flag] is not None:
                return memo[i][flag]
            if flag:
                memo[i][flag] = max(0, nums[i] + dfs(i + 1, True))
            else:
                memo[i][flag] = max(dfs(i + 1, False),
                                    nums[i] + dfs(i + 1, True))
            return memo[i][flag]

        return dfs(0, False)

    def max_sub_array_v3(self, nums: List[int]) -> int:
        def dfs(i, flag):
            if i == len(nums):
                return 0 if flag else -1e6
            if flag:
                return max(0, nums[i] + dfs(i + 1, True))
            return max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))

        return dfs(0, False)

    def max_sub_array_v4(self, nums: List[int]) -> int:
        dp = [*nums]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([1], 1),
            ([5, 4, -1, 7, 8], 23),
            ([-1, -2, -3], -1),
            ([0, 0, 0], 0),
            ([-1, 2, 3, -4, 5], 6),
            ([1, 2, 3], 6),
            ([3, -2, 5], 6),
            ([-2, -1], -1)
        ]

    def test_max_sub_array(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                result = self.solution.max_sub_array(nums)
                self.assertEqual(result, expected)

    def test_max_sub_array_v2(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                result = self.solution.max_sub_array_v2(nums)
                self.assertEqual(result, expected)

    def test_max_sub_array_v3(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                result = self.solution.max_sub_array_v3(nums)
                self.assertEqual(result, expected)

    def test_max_sub_array_v4(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                result = self.solution.max_sub_array_v4(nums)
                self.assertEqual(result, expected)
