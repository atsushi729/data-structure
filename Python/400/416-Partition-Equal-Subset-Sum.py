from typing import List
import unittest


class Solution:
    def can_partition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        def dfs(i, target):
            if i >= len(nums):
                return target == 0
            if target < 0:
                return False

            return dfs(i + 1, target) or dfs(i + 1, target - nums[i])

        return dfs(0, sum(nums) // 2)

    def can_partition_v2(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            memo[i][target] = (dfs(i + 1, target) or dfs(i + 1, target - nums[i]))
            return memo[i][target]

        return dfs(0, target)


class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_can_partition(self):
        self.assertTrue(self.solution.can_partition([1, 5, 11, 5]))
        self.assertFalse(self.solution.can_partition([1, 2, 3, 5]))

    def test_can_partition_v2(self):
        self.assertTrue(self.solution.can_partition_v2([1, 5, 11, 5]))
        self.assertFalse(self.solution.can_partition_v2([1, 2, 3, 5]))
