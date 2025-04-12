from typing import List
import unittest


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]

        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                res = max(res, cur)
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([1], 1),
            ([5, 4, -1, 7, 8], 23),
            ([-1, -2, -3], -1),
            ([0, 0, 0], 0),
            ([-1, 2, 3, -4, 5], 6),
            ([1, 2, 3], 6),
            ([3, -2, 5], 6),
            ([-2, -1], -1)
        ]

    def test_max_sub_array(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                result = self.solution.max_sub_array(nums)
                self.assertEqual(result, expected)
