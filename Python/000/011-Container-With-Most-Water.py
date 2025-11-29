import unittest


#################### Solution ####################
class Solution:
    def max_area(self, heights: list[int]) -> int:
        max_amount = 0
        left, right = 0, len(heights) - 1

        while left < right:
            width = right - left
            min_height = min(heights[left], heights[right])
            current_amount = width * min_height

            max_amount = max(max_amount, current_amount)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_amount

    def model_max_area(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res

    def max_area_v2(self, heights: list[int]) -> int:
        res = 0
        n = len(heights)

        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res


#################### Test Case ####################
class TestMaxArea(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
            ([1, 1], 1),
            ([4, 3, 2, 1, 4], 16),
            ([1, 2, 1], 2),
        ]

    def test_max_area(self):
        for heights, expected in self.test_cases:
            with self.subTest(heights=heights):
                result = self.s.max_area(heights)
                self.assertEqual(result, expected)

    def test_model_max_area(self):
        for heights, expected in self.test_cases:
            with self.subTest(heights=heights):
                result = self.s.model_max_area(heights)
                self.assertEqual(result, expected)

    def test_max_area_v2(self):
        for heights, expected in self.test_cases:
            with self.subTest(heights=heights):
                result = self.s.max_area_v2(heights)
                self.assertEqual(result, expected)
