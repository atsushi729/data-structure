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
