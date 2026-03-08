import unittest


#################### Solution ####################
class Solution:
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left = 0
        right = m

        while left <= right:

            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            left1 = float('-inf') if i == 0 else nums1[i-1]
            right1 = float('inf') if i == m else nums1[i]

            left2 = float('-inf') if j == 0 else nums2[j-1]
            right2 = float('inf') if j == n else nums2[j]

            if left1 <= right2 and left2 <= right1:

                if (m + n) % 2 == 0:
                    return (max(left1,left2) + min(right1,right2)) / 2
                else:
                    return max(left1,left2)

            elif left1 > right2:
                right = i - 1

            else:
                left = i + 1


#################### Test Case ####################
class TestFindMedianSortedArrays(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([1, 3], [2], 2.0),
            ([1, 2], [3, 4], 2.5),
            ([0, 0], [0, 0], 0.0),
            ([], [1], 1.0),
            ([2], [], 2.0)
        ]

    def test_find_median_sorted_arrays(self):
        for nums1, nums2, expected in self.test_cases:
            with self.subTest(nums1=nums1, nums2=nums2, expected=expected):
                self.assertEqual(self.s.find_median_sorted_arrays(nums1, nums2), expected)
