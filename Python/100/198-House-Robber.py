from typing import List
import unittest


#################### Solution ####################
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    def rob_v2(self, nums: List[int]) -> int:
        def dfs(i):
            if i >= len(nums):
                return 0
            return nums[i] + max(dfs(i + 2), dfs(i + 3))

        return dfs(0)


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_rob(self):
        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4)
        self.assertEqual(self.solution.rob([2, 7, 9, 3, 1]), 12)
        self.assertEqual(self.solution.rob([2, 1, 1, 2]), 4)

    def test_rob_v2(self):
        self.assertEqual(self.solution.rob_v2([1, 2, 3, 1]), 4)
        self.assertEqual(self.solution.rob_v2([2, 7, 9, 3, 1]), 12)
        self.assertEqual(self.solution.rob_v2([2, 1, 1, 2]), 4)
