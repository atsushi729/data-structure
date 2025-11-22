import unittest
from typing import List


class Solution:
    def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Time complexity: O(n^4)
        Space complexity: O(n)
        """
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

    def four_sum_v2(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Time complexity: O(n^3)
        Space complexity: O(n)
        """
        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n):
            for j in range(i + 1, n):
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        res.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
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

    def test_four_sum_v2(self):
        for nums, target, expected in self.test_cases:
            with self.subTest(nums=nums, target=target):
                result = self.s.four_sum_v2(nums, target)
                result_sorted = [sorted(quad) for quad in result]
                expected_sorted = [sorted(quad) for quad in expected]
                self.assertCountEqual(result_sorted, expected_sorted)
