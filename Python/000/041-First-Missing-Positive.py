import unittest
from typing import List


class Solution:
    def first_missing_positive(self, nums: List[int]) -> int:
        # Replace negative numbers with 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        # Use index as a hash to record the frequency of each number
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        # The first index with a positive value indicates the missing positive integer
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i

        return len(nums) + 1

    def first_missing_positive_v2(self, nums: List[int]) -> int:
        missing = 1
        while True:
            found = False
            for num in nums:
                if num == missing:
                    found = True
                    break
            if not found:
                return missing
            missing += 1

    def first_missing_positive_v3(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [False] * n

        for num in nums:
            if 0 < num <= n:
                seen[num - 1] = True

        for num in range(1, n + 1):
            if not seen[num - 1]:
                return num

        return n + 1

    def first_missing_positive_v4(self, nums: List[int]) -> int:
        nums.sort()
        missing = 1

        for num in nums:
            if 0 < num == missing:
                missing += 1
        return missing

    def first_missing_positive_v5(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] <= 0 or nums[i] > n:
                i += 1
                continue
            index = nums[i] - 1

            if nums[i] != nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            ([1, 2, 0], 3),
            ([3, 4, -1, 1], 2),
            ([7, 8, 9, 11, 12], 1),
            ([1, 1], 2),
            ([2, 2], 1),
            ([1], 2),
            ([], 1),
        ]

    def test_first_missing_positive(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(self.s.first_missing_positive(nums.copy()), expected)

    def test_first_missing_positive_v2(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(self.s.first_missing_positive_v2(nums.copy()), expected)

    def test_first_missing_positive_v3(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(self.s.first_missing_positive_v3(nums.copy()), expected)

    def test_first_missing_positive_v4(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(self.s.first_missing_positive_v4(nums.copy()), expected)

    def test_first_missing_positive_v5(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(self.s.first_missing_positive_v5(nums.copy()), expected)
