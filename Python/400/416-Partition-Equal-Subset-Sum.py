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


class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_can_partition(self):
        self.assertTrue(self.solution.can_partition([1, 5, 11, 5]))
        self.assertFalse(self.solution.can_partition([1, 2, 3, 5]))
