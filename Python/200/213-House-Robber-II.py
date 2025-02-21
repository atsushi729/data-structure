from typing import List
import unittest


#################### Solution ####################
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            tmp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_rob(self):
        solution = Solution()
        self.assertEqual(solution.rob([1, 2, 3, 1]), 4)
        self.assertEqual(solution.rob([2, 7, 9, 3, 1]), 11)
        self.assertEqual(solution.rob([2, 1, 1, 2]), 3)
