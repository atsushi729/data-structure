import unittest


#################### Solution ####################
class Solution:
    def find_min(self, nums: list[int]) -> int:
        """
        Time complexity: O(log n)
        Space complexity: O(1)
        """
        start, end = 0, len(nums) - 1
        curr_min = float("inf")

        while start < end:
            mid = (start + end) // 2
            curr_min = min(curr_min, nums[mid])

            # right has the min
            if nums[mid] > nums[end]:
                start = mid + 1

            # left has the  min
            else:
                end = mid - 1

        return min(curr_min, nums[start])

    def find_min_v2(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        return min(nums)

    def find_min_v3(self, nums: list[int]) -> int:
        """
        Time complexity: O(log n)
        Space complexity: O(1)
        """
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res

    def find_min_v4(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


#################### Test Case ####################
class TestFindMin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([3, 4, 5, 6, 1, 2], 1),
            ([4, 1, 2, 3], 1),
            ([4, 5, 6, 7, 0, 1, 2], 0),
            ([11, 13, 15, 17], 11),
            ([2, 1], 1),
        ]

    def test_find_min(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                result = self.s.find_min(nums)
                self.assertEqual(result, expected)

    def test_find_min_v2(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                result = self.s.find_min_v2(nums)
                self.assertEqual(result, expected)

    def test_find_min_v3(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                result = self.s.find_min_v3(nums)
                self.assertEqual(result, expected)

    def test_find_min_v4(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                result = self.s.find_min_v4(nums)
                self.assertEqual(result, expected)
