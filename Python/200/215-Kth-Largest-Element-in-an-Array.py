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

    def find_kth_largest_v4(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)

        res = heapq.heappop(nums)
        return res * -1


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("base case", [3, 2, 1, 5, 6, 4], 2, 5),
            ("with duplicates", [3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
            ("k is 1", [3, 2, 1, 5, 6, 4], 1, 6),
            ("k is len(nums)", [3, 2, 1, 5, 6, 4], 6, 1),
            ("single element", [1], 1, 1),
            ("negative numbers", [-1, -2, -3, -4], 2, -2),
        ]

    def test_find_kth_largest(self):
        for name, nums, k, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(expected, self.solution.find_kth_largest(nums[:], k))

    def test_find_kth_largest_v2(self):
        for name, nums, k, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(expected, self.solution.find_kth_largest_v2(nums[:], k))

    def test_find_kth_largest_v3(self):
        for name, nums, k, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(expected, self.solution.find_kth_largest_v3(nums[:], k))

    def test_find_kth_largest_v4(self):
        for name, nums, k, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(expected, self.solution.find_kth_largest_v4(nums[:], k))
