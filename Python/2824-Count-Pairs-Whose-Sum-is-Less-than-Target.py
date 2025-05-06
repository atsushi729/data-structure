from typing import List
import unittest


class Solution:
    def count_pairs(self, nums: List[int], target: int) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1

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
