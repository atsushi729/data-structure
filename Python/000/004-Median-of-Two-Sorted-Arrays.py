import unittest


#################### Solution ####################
class Solution:
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


#################### Test Case ####################
class TestFindMedianSortedArrays(unittest.TestCase):
    def test_find_median_sorted_arrays(self):
        solution = Solution()
        self.assertEqual(solution.find_median_sorted_arrays([1, 3], [2]), 2.0)
        self.assertEqual(solution.find_median_sorted_arrays([1, 2], [3, 4]), 2.5)
        self.assertEqual(solution.find_median_sorted_arrays([0, 0], [0, 0]), 0.0)
        self.assertEqual(solution.find_median_sorted_arrays([], [1]), 1.0)
        self.assertEqual(solution.find_median_sorted_arrays([2], []), 2.0)
