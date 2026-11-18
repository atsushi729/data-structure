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
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

        cls.methods = [
            cls.solution.my_sqrt,
            cls.solution.my_sqrt_v2,
        ]

        cls.test_cases = [
            # Zero and one
            (0, 0),
            (1, 1),

            # Small numbers
            (2, 1),
            (3, 1),
            (4, 2),
            (5, 2),
            (8, 2),
            (9, 3),

            # Non-perfect squares
            (15, 3),
            (17, 4),
            (24, 4),
            (26, 5),
            (35, 5),
            (99, 9),
            (101, 10),

            # Perfect squares
            (16, 4),
            (25, 5),
            (36, 6),
            (49, 7),
            (64, 8),
            (100, 10),
            (10000, 100),

            # Boundary cases
            (2147395599, 46339),
            (2147395600, 46340),
            (2147483647, 46340),

            # Large numbers
            (10 ** 12, 10 ** 6),
            (10 ** 12 - 1, 10 ** 6 - 1),
            (10 ** 18, 10 ** 9),
            (10 ** 18 - 1, 10 ** 9 - 1),
        ]

    def test_my_sqrt(self):
        for method in self.methods:
            for x, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        x=x,
                ):
                    result = method(x)
                    self.assertEqual(
                        result,
                        expected,
                        f"{method.__name__}({x}): "
                        f"expected {expected}, got {result}",
                    )


if __name__ == "__main__":
    unittest.main()
