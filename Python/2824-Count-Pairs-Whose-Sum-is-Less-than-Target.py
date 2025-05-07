from typing import List
import unittest


class Solution:
    def count_pairs(self, nums: List[int], target: int) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1

        return count

    def count_pairs_v2(self, nums: List[int], target: int) -> int:
        """
        Time complexity: O(n log n)
        Space complexity: O(1)
        """
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1

        return count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            ([1, 2, 3, 4], 5, 2),
            ([1, 2, 3], 3, 0),
            ([1, 2, 3], 6, 3),
            ([0, -1, -2], -1, 2),
            ([], 0, 0),
            ([1], 2, 0),
            ([1, 2], 3, 0),
        ]

    def test_count_pairs(self):
        for nums, target, expected in self.test_cases:
            result = self.solution.count_pairs(nums, target)
            self.assertEqual(result, expected)

    def test_count_pairs_v2(self):
        for nums, target, expected in self.test_cases:
            result = self.solution.count_pairs_v2(nums, target)
            self.assertEqual(result, expected)
