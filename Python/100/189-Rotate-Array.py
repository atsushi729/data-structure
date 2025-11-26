from typing import List
import unittest


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        while k:
            tmp = nums[n - 1]
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = tmp
            k -= 1

    def rotate_v2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
            ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
            ([1, 2], 3, [2, 1]),
        ]

    def test_rotate(self):
        for nums, k, expected in self.test_cases:
            with self.subTest(nums=nums, k=k, expected=expected):
                arr = nums[:]
                self.s.rotate(arr, k)
                self.assertEqual(arr, expected)

    def test_rotate_v2(self):
        for nums, k, expected in self.test_cases:
            with self.subTest(nums=nums, k=k, expected=expected):
                arr = nums[:]
                self.s.rotate_v2(arr, k)
                self.assertEqual(arr, expected)
