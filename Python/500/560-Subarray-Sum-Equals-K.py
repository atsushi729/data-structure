from typing import List
import unittest


class Solution:
    def subarray_sum(self, nums: List[int], k: int) -> int:
        res = 0

        for i in range(len(nums)):
            sum = 0

            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    res += 1

        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            ([1, 1, 1], 2, 2),
            ([1, 2, 3], 3, 2),
            ([1, -1, 0], 0, 3),
            ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
            ([1, 2, 1, 2, 1], 3, 4),
        ]

    def test_subarraySum(self):
        for nums, k, expected in self.test_cases:
            with self.subTest(nums=nums, k=k, expected=expected):
                self.assertEqual(self.s.subarray_sum(nums, k), expected)
