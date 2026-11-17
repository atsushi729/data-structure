import unittest


class Solution:
    def my_sqrt(self, x: int) -> int:
        """
        Binary Search
        Time Complexity: O(log x)
        Space Complexity: O(1)
        """
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

    def my_sqrt_v2(self, x: int) -> int:
        """
        Newton's Method
        Time Complexity: O(log log x)
        Space Complexity: O(1)
        """
        if x < 2:
            return x

        r = x

        while r > x // r:
            r = (r + x // r) // 2

        return r


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 1),
            (4, 2),
            (8, 2),
            (15, 3),
            (16, 4),
            (24, 4),
            (25, 5),
            (26, 5),
            (99, 9),
            (100, 10),
            (2147395599, 46339),
            (2147483647, 46340),
        ]

    def test_my_sqrt(self):
        for x, expected in self.test_cases:
            with self.subTest(x=x):
                self.assertEqual(self.solution.my_sqrt(x), expected)

    def test_my_sqrt_v2(self):
        for x, expected in self.test_cases:
            with self.subTest(x=x):
                self.assertEqual(self.solution.my_sqrt_v2(x), expected)
