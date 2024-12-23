import unittest
from typing import List
import heapq


#################### Solution ####################
class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    def find_kth_largest_v2(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_find_kth_largest(self):
        solution = Solution()
        self.assertEqual(solution.find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(solution.find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_find_kth_largest_v2(self):
        solution = Solution()
        self.assertEqual(solution.find_kth_largest_v2([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(solution.find_kth_largest_v2([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)