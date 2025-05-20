from typing import List
import unittest


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        return expected_sum - sum(nums)

    def missingNumber_v2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] != i:
                return i
        return n


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            ([3, 0, 1], 2),
            ([0, 1], 2),
            ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
            ([0], 1),
            ([], 0),
            ([1], 0),
        ]

    def test_missingNumber(self):
        for nums, expected in self.test_cases:
            result = self.solution.missingNumber(nums)
            self.assertEqual(result, expected)

    def test_missingNumber_v2(self):
        for nums, expected in self.test_cases:
            result = self.solution.missingNumber_v2(nums)
            self.assertEqual(result, expected)