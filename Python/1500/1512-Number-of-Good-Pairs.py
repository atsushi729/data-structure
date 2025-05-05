from collections import Counter
from typing import List
import unittest


class Solution:
    def num_identical_pairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        count = 0
        for v in freq.values():
            count += v * (v - 1) // 2
        return count

    def num_identical_pairs_v2(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count

    def num_identical_pairs_v3(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return sum(v * (v - 1) // 2 for v in freq.values())


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            ([1, 2, 3, 1, 1, 3], 4),
            ([1, 1, 1, 1], 6),
            ([1, 2, 3], 0),
            ([1], 0),
            ([], 0),
            ([1, 2, 2, 3, 3], 2),
        ]

    def test_num_identical_pairs(self):
        for nums, expected in self.test_cases:
            result = self.solution.num_identical_pairs(nums)
            self.assertEqual(result, expected)

    def test_num_identical_pairs_v2(self):
        for nums, expected in self.test_cases:
            result = self.solution.num_identical_pairs_v2(nums)
            self.assertEqual(result, expected)

    def test_num_identical_pairs_v3(self):
        for nums, expected in self.test_cases:
            result = self.solution.num_identical_pairs_v3(nums)
            self.assertEqual(result, expected)
