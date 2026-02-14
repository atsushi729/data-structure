import unittest


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

    def search_v2(self, nums: list[int], target: int) -> int:
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

    def binary_search(self, left: int, right: int, nums: list[int], target: int) -> int:
        if left > right:
            return -1
        m = left + (right - left) // 2

        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.binary_search(m + 1, right, nums, target)
        return self.binary_search(left, m - 1, nums, target)

    def search_v3(self, nums: list[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)


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
            with self.subTest(nums=nums, target=target, expected=expected):
                self.assertEqual(self.s.search_v2(nums, target), expected)

    def test_search_v3(self):
        for nums, target, expected in self.test_cases:
            with self.subTest(nums=nums, target=target, expected=expected):
                self.assertEqual(self.s.search_v3(nums, target), expected)
