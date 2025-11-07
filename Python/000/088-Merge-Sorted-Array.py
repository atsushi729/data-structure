import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
            ([1], 1, [], 0, [1]),
            ([0], 0, [1], 1, [1]),
            ([2, 0], 1, [1], 1, [1, 2]),
            ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        ]

    def test_merge(self):
        for nums1, m, nums2, n, expected in self.test_cases:
            with self.subTest(
                    nums1=nums1, m=m, nums2=nums2, n=n, expected=expected
            ):
                self.s.merge(nums1, m, nums2, n)
                self.assertEqual(nums1, expected)
