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

    def find_kth_largest_v3(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quick_select(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quick_select(l, p - 1)
            elif p < k:
                return quick_select(p + 1, r)
            else:
                return nums[p]

        return quick_select(0, len(nums) - 1)


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

    def test_find_kth_largest_v3(self):
        solution = Solution()
        self.assertEqual(solution.find_kth_largest_v3([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(solution.find_kth_largest_v3([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
