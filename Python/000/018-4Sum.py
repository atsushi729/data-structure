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

    def four_sum_v3(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Time complexity: O(n^(k-1))
        Space complexity: O(n)
        """
        nums.sort()
        res, quad = [], []

        def k_sum(k, start, target):
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                return

            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                k_sum(k - 1, i + 1, target - nums[i])
                quad.pop()

        k_sum(4, 0, target)
        return res

    def four_sum_v4(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Time complexity: O(n^(k-1))
        Space complexity: O(n)
        """
        nums.sort()
        res, quad = [], []

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return

            # base case, two sum II
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        kSum(4, 0, target)
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
            ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
            ([], 0, []),
            ([0, 0, 0, 0], 0, [[0, 0, 0, 0]]),
            ([1, 2, 3, 4], 10, [[1, 2, 3, 4]]),
            ([1, 2, 3, 4], 100, []),
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

    def test_four_sum_v3(self):
        for nums, target, expected in self.test_cases:
            with self.subTest(nums=nums, target=target):
                result = self.s.four_sum_v3(nums, target)
                result_sorted = [sorted(quad) for quad in result]
                expected_sorted = [sorted(quad) for quad in expected]
                self.assertCountEqual(result_sorted, expected_sorted)

    def test_four_sum_v4(self):
        for nums, target, expected in self.test_cases:
            with self.subTest(nums=nums, target=target):
                result = self.s.four_sum_v4(nums, target)
                result_sorted = [sorted(quad) for quad in result]
                expected_sorted = [sorted(quad) for quad in expected]
                self.assertCountEqual(result_sorted, expected_sorted)
