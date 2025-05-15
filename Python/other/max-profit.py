from collections import defaultdict
from typing import List
import unittest


class Solution:
    def count_two_sum_pairs(self, nums: List[int], target: int) -> int:
        count = 0
        num_map = defaultdict(int)

        for num in nums:
            complement = target - num
            if num_map[complement] > 0:
                count += 1
                num_map[complement] -= 1
            else:
                num_map[num] += 1

        return count

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            ([1, 2, 3, 4], 5, 2),
            ([1, 1, 2, 2], 3, 2),
            ([1, 2, 3, 4], 6, 1),
            ([0, -1, 1], 0, 1),
            ([5, -5, 5], 0, 1),
            ([], 0, 0),
            ([1], 2, 0),
        ]

    def test_count_two_sum_pairs(self):
        for nums, target, expected in self.test_cases:
            result = self.solution.count_two_sum_pairs(nums, target)
            self.assertEqual(result, expected)
