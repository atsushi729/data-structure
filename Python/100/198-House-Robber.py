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


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_rob(self):
        solution = Solution()
        self.assertEqual(solution.rob([1, 2, 3, 1]), 4)
        self.assertEqual(solution.rob([2, 7, 9, 3, 1]), 12)
        self.assertEqual(solution.rob([2, 1, 1, 2]), 4)
