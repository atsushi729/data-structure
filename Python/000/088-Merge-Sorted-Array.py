import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[:n]
        nums1.sort()

    def merge_v2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_copy = nums1[:m]
        idx = 0
        i = j = 0

        while idx < m + n:
            if j >= n or (i < len(nums1_copy) and nums1_copy[i] <= nums2[j]):
                nums1[idx] = nums1_copy[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1
            idx += 1

    def merge_v3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

    def merge_v4(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1
        i, j = m - 1, n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1

            last -= 1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        self.test_cases = [
            ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
            ([1], 1, [], 0, [1]),
            ([0], 0, [1], 1, [1]),
            ([2, 0], 1, [1], 1, [1, 2]),
            ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        ]

    def test_merge(self):
        for nums1, m, nums2, n, expected in self.test_cases:
            nums1_copy = nums1.copy()
            self.s.merge(nums1_copy, m, nums2, n)
            self.assertEqual(nums1_copy, expected)

    def test_merge_v2(self):
        for nums1, m, nums2, n, expected in self.test_cases:
            nums1_copy = nums1.copy()
            self.s.merge_v2(nums1_copy, m, nums2, n)
            self.assertEqual(nums1_copy, expected)

    def test_merge_v3(self):
        for nums1, m, nums2, n, expected in self.test_cases:
            nums1_copy = nums1.copy()
            self.s.merge_v3(nums1_copy, m, nums2, n)
            self.assertEqual(nums1_copy, expected)

    def test_merge_v4(self):
        for nums1, m, nums2, n, expected in self.test_cases:
            nums1_copy = nums1.copy()
            self.s.merge_v4(nums1_copy, m, nums2, n)
            self.assertEqual(nums1_copy, expected)
