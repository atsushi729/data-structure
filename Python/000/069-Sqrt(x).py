import unittest


class Solution:
    def my_sqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            (4, 2),
            (8, 2),
            (0, 0),
            (1, 1),
            (16, 4),
            (15, 3),
            (25, 5),
            (26, 5),
        ]

    def test_my_sqrt(self):
        for x, expected in self.test_cases:
            result = self.solution.my_sqrt(x)
            self.assertEqual(result, expected)
