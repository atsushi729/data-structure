import unittest


#################### Solution ####################
def max_area(heights: list[int]) -> int:
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


def model_max_area(heights: list[int]) -> int:
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


#################### Test Case ####################
class TestMaxArea(unittest.TestCase):
    def test_max_area(self):
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_model_max_area(self):
        self.assertEqual(model_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
