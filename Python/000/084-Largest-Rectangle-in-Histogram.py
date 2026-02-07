import unittest


#################### Solution ####################
class Solution:
    def largest_rectangle_area(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
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

    def largest_rectangle_area_v2(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        max_area = 0
        stack = []

        for i in range(len(heights) + 1):
            current_height = heights[i] if i < len(heights) else 0
            start_index = i

            while stack and stack[-1][1] > current_height:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start_index = index
            stack.append((start_index, current_height))

        return max_area

    def largest_rectangle_area_v3(self, heights: list[int]) -> int:
        max_area = 0
        stack = []  # pair: (left_boundary, height)

        for current_index, current_height in enumerate(heights):
            left_boundary = current_index

            while stack and stack[-1][1] > current_height:
                prev_index, prev_height = stack.pop()
                max_area = max(max_area, prev_height * (current_index - prev_index))
                left_boundary = prev_index
            stack.append((left_boundary, current_height))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([2, 1, 5, 6, 2, 3], 10),
            ([2, 4], 4),
            ([6, 2, 5, 4, 5, 1, 6], 12),
            ([1, 1], 2),
            ([4, 2, 0, 3, 2, 5], 6),
        ]

    def test_largest_rectangle_area(self):
        for heights, expected in self.test_cases:
            self.assertEqual(
                self.s.largest_rectangle_area(heights),
                expected
            )

    def test_largest_rectangle_area_v2(self):
        for heights, expected in self.test_cases:
            self.assertEqual(
                self.s.largest_rectangle_area_v2(heights),
                expected
            )

    def test_largest_rectangle_area_v3(self):
        for heights, expected in self.test_cases:
            self.assertEqual(
                self.s.largest_rectangle_area_v3(heights),
                expected
            )
