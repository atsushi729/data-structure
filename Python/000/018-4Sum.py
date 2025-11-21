import unittest
from typing import List


class Solution:
    def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()

        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        if nums[a] + nums[b] + nums[c] + nums[d] == target:
                            res.add((nums[a], nums[b], nums[c], nums[d]))
        return list(res)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
            ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        ]

    def test_four_sum(self):
        for nums, target, expected in self.test_cases:
            with self.subTest(nums=nums, target=target):
                result = self.s.four_sum(nums, target)
                result_sorted = [sorted(quad) for quad in result]
                expected_sorted = [sorted(quad) for quad in expected]
                self.assertCountEqual(result_sorted, expected_sorted)