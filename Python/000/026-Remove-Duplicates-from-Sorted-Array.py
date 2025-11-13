import unittest
from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        position = 1

        # Edge case: empty list
        if len(nums) == 0:
            return 0

        # Iterate through the list and move unique elements to the front
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[position] = nums[i]
                position += 1

        return position


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            # ([1, 1, 2], 2, [1, 2]),
            ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
            ([], 0, []),
            ([1, 2, 3], 3, [1, 2, 3]),
            ([1, 1, 1, 1], 1, [1]),
        ]

    def test_remove_duplicates(self):
        for nums, expected_length, expected_nums in self.test_cases:
            with self.subTest(nums=nums):
                length = self.s.remove_duplicates(nums)
                self.assertEqual(length, expected_length)
                self.assertEqual(nums[:length], expected_nums)