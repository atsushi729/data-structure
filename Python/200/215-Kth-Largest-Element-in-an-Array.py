import unittest
from typing import List
import heapq


#################### Solution ####################
class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_find_kth_largest(self):
        solution = Solution()
        self.assertEqual(solution.find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(solution.find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
