from typing import List
import unittest


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(i, j):
            if i == len(nums):
                return 0

            LIS = dfs(i + 1, j)  # not include

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))  # include

            return LIS

        return dfs(0, -1)

    def lengthOfLIS_v2(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, j):
            if i == n:
                return 0
            if memo[i][j + 1] != -1:
                return memo[i][j + 1]

            LIS = dfs(i + 1, j)

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))

            memo[i][j + 1] = LIS
            return LIS

        return dfs(0, -1)

    def lengthOfLIS_v3(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)


class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_lengthOfLIS(self):
        self.assertEqual(self.solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(self.solution.lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)
        self.assertEqual(self.solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1)

    def test_lengthOfLIS_v2(self):
        self.assertEqual(self.solution.lengthOfLIS_v2([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(self.solution.lengthOfLIS_v2([0, 1, 0, 3, 2, 3]), 4)
        self.assertEqual(self.solution.lengthOfLIS_v2([7, 7, 7, 7, 7, 7, 7]), 1)

    def test_lengthOfLIS_v3(self):
        self.assertEqual(self.solution.lengthOfLIS_v3([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(self.solution.lengthOfLIS_v3([0, 1, 0, 3, 2, 3]), 4)
        self.assertEqual(self.solution.lengthOfLIS_v3([7, 7, 7, 7, 7, 7, 7]), 1)
