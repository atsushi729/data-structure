import unittest
from typing import List


class Solution:
    def first_missing_positive(self, nums: List[int]) -> int:
        # Replace negative numbers with 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        # Use index as a hash to record the frequency of each number
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        # The first index with a positive value indicates the missing positive integer
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i

        return len(nums) + 1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            ([1, 2, 0], 3),
            ([3, 4, -1, 1], 2),
            ([7, 8, 9, 11, 12], 1),
            ([1, 1], 2),
            ([2, 2], 1),
            ([1], 2),
            ([], 1),
        ]

    def test_firstMissingPositive(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(self.s.first_missing_positive(nums), expected)
