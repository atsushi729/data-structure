import unittest
import math


class Solution:
    def my_pow(self, x: float, n: int) -> float:
        """
        Time: O(|n|)
        Space: O(1)
        """
        if n == 0:
            return 1.0
        if x == 0:
            if n < 0:
                raise ZeroDivisionError("0 cannot be raised to a negative power")
            return 0.0

        if n < 0:
            x = 1.0 / x
            n = -n

        res = 1.0
        for _ in range(n):
            res *= x

        return res

    def my_pow2(self, x: float, n: int) -> float:
        """
        Time: O(log |n|)
        Space: O(log |n|)
        Recursive Binary Exponentiation
        """

        def helper(x, n):
            if n == 0:
                return 1.0

            res = helper(x * x, n // 2)
            return x * res if n % 2 else res

        if n == 0:
            return 1.0
        if x == 0:
            if n < 0:
                raise ZeroDivisionError("0 cannot be raised to a negative power")
            return 0.0

        if n < 0:
            x = 1.0 / x
            n = -n

        return helper(x, n)

    def my_pow3(self, x: float, n: int) -> float:
        """
        Time: O(log |n|)
        Space: O(1)
        Iterative Binary Exponentiation
        """
        if n == 0:
            return 1.0
        if x == 0:
            if n < 0:
                raise ZeroDivisionError("0 cannot be raised to a negative power")
            return 0.0

        if n < 0:
            x = 1.0 / x
            n = -n

        res = 1.0

        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1

        return res

    def my_pow4(self, x: float, n: int) -> float:
        """
        Time: O(log |n|)
        Space: O(1)
        Optimized Binary Exponentiation
        """
        if n == 0:
            return 1.0
        if x == 1.0:
            return 1.0
        if x == -1.0:
            return 1.0 if (n & 1) == 0 else -1.0

        if x == 0:
            if n < 0:
                raise ZeroDivisionError("0 cannot be raised to a negative power")
            return 0.0

        if n < 0:
            x = 1.0 / x
            n = -n

        res = 1.0

        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1

        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

        cls.methods = [
            cls.solution.my_pow,
            cls.solution.my_pow2,
            cls.solution.my_pow3,
            cls.solution.my_pow4,
        ]

        cls.test_cases = [
            # Basic cases
            (2.0, 10, 1024.0),
            (2.1, 3, 9.261),
            (2.0, -2, 0.25),
            (0.44528, 0, 1.0),

            # Zero exponent
            (2.0, 0, 1.0),
            (-2.0, 0, 1.0),
            (0.0, 0, 1.0),

            # Zero base
            (0.0, 1, 0.0),
            (0.0, 5, 0.0),

            # Negative base
            (-2.0, 3, -8.0),
            (-2.0, 4, 16.0),
            (-2.0, -3, -0.125),
            (-2.0, -4, 0.0625),

            # Exponent of one
            (5.0, 1, 5.0),
            (5.0, -1, 0.2),

            # Base of one
            (1.0, 100, 1.0),
            (1.0, -100, 1.0),
            (-1.0, 101, -1.0),
            (-1.0, 100, 1.0),

            # Fractional base
            (0.5, 3, 0.125),
            (0.5, -3, 8.0),

            # Large exponent
            (2.0, 20, 1048576.0),
            (2.0, -10, 0.0009765625),

            # Additional edge cases
            (2.0, -20, 2.0 ** -20),
            (0.1, -3, 1000.0),
            (-0.5, -3, -8.0),
        ]

    def test_my_pow(self):
        for method in self.methods:
            for x, n, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        x=x,
                        n=n,
                ):
                    result = method(x, n)
                    self.assertTrue(
                        math.isclose(
                            result,
                            expected,
                            rel_tol=1e-9,
                            abs_tol=1e-9,
                        ),
                        f"{method.__name__}({x}, {n}): "
                        f"expected {expected}, got {result}",
                    )

    def test_zero_negative_exponent(self):
        for method in self.methods:
            with self.subTest(method=method.__name__):
                with self.assertRaises(ZeroDivisionError):
                    method(0.0, -1)
