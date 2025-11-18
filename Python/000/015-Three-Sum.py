import unittest
from collections import defaultdict


#################### Solution ####################
class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]

    def three_sum_v2(self, nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res

    def three_sum_v3(self, nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        nums.sort()
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        res = []

        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue

                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res


#################### Test Case ####################
class TestThreeSum(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        self.test_cases = [
            # (nums, expected)
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([0, 1, 1], []),
            ([0, 0, 0], [[0, 0, 0]]),
        ]

    def test_threeSum(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                result = self.s.three_sum(nums)
                result_sorted = [sorted(triplet) for triplet in result]
                expected_sorted = [sorted(triplet) for triplet in expected]
                self.assertCountEqual(result_sorted, expected_sorted)

    def test_threeSum_v2(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                result = self.s.three_sum_v2(nums)
                result_sorted = [sorted(triplet) for triplet in result]
                expected_sorted = [sorted(triplet) for triplet in expected]
                self.assertCountEqual(result_sorted, expected_sorted)

    def test_threeSum_v3(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                result = self.s.three_sum_v3(nums)
                result_sorted = [sorted(triplet) for triplet in result]
                expected_sorted = [sorted(triplet) for triplet in expected]
                self.assertCountEqual(result_sorted, expected_sorted)