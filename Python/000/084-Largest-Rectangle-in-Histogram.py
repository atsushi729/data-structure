import unittest


#################### Solution ####################
def largest_rectangle_area(heights: list[int]) -> int:
    max_area = 0
    stack = []

    for i, h in enumerate(heights):
        start = i

        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))

    return max_area


#################### Test Case ####################
class TestLargestRectangleArea(unittest.TestCase):
    def test_largest_rectangle_area(self):
        self.assertEqual(largest_rectangle_area([2, 1, 5, 6, 2, 3]), 10)
        self.assertEqual(largest_rectangle_area([2, 4]), 4)
        self.assertEqual(largest_rectangle_area([2, 1, 2]), 3)
        self.assertEqual(largest_rectangle_area([2, 1, 5, 6, 2, 3]), 10)
        self.assertEqual(largest_rectangle_area([2, 1, 5, 6, 2, 3, 1, 2]), 10)
