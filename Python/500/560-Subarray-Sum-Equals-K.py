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

    def subarray_sum_v2(self, nums: List[int], k: int) -> int:
        prefix_sum_count = {0: 1}
        prefix_sum = 0
        res = 0

        for num in nums:
            prefix_sum += num
            complement = prefix_sum - k

            res += prefix_sum_count.get(complement, 0)
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1

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

    def test_subarraySum_v2(self):
        for nums, k, expected in self.test_cases:
            with self.subTest(nums=nums, k=k, expected=expected):
                self.assertEqual(self.s.subarray_sum_v2(nums, k), expected)
