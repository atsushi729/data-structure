import unittest
from typing import List


#################### Solution ####################
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def search_v2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            # Avoid overflow for C++/Java
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


#################### Test Case ####################
class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([-1, 0, 3, 5, 9, 12], 9, 4),
            ([-1, 0, 3, 5, 9, 12], 2, -1),
            ([5], 5, 0),
            ([1, 2, 3, 4, 5], 1, 0),
            ([1, 2, 3, 4, 5], 5, 4),
        ]

    def test_search(self):
        for nums, target, expected in self.test_cases:
            with self.subTest(nums=nums, target=target, expected=expected):
                self.assertEqual(self.s.search(nums, target), expected)

    def test_search_v2(self):
        for nums, target, expected in self.test_cases:
            with self.subTest(nums=nums, target=target, exptected=expected):
                self.assertEqual(self.s.search_v2(nums, target), expected)