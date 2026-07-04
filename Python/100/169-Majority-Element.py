import unittest
from collections import Counter


class Solution:
    def majority_element(self, nums: list[int]) -> int:
        frequency = len(nums) / 2
        counter = Counter(nums)

        for k, v in counter.items():
            if v > frequency:
                return k
        return 0


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([2, 2, 3], 2),
            ([3, 3], 3),
        ]

    def test_majority_element(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.majority_element(nums), expected)
