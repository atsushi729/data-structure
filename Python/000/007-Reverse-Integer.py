import unittest
import math


class Solution:
    def reverse(self, x: int) -> int:
        org = x
        x = abs(x)
        res = int(str(x)[::-1])

        if org < 0:
            res *= -1
        if res < -(1 << 31) or res > (1 << 31) - 1:
            return 0
        return res

    def reverse_v2(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647
        res = 0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit

        return res

    def reverse_v3(self, x: int) -> int:
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        res = 0

        while x != 0:
            # Get the last digit
            digit = int(math.fmod(x, 10))
            # Remove the last digit from x
            x = int(x / 10)

            # Check for overflow
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            # Update the result
            res = res * 10 + digit

        return res

    def reverse_v4(self, x: int) -> int:
        """
        This method is similar to reverse_v3 but uses string manipulation.
        """
        MAX = 2 ** 31 - 1
        MIN = -2 ** 31

        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x = x // 10

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0

            res = res * 10 + digit

        return sign * res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            # (123, 321),
            # (-123, -321),
            # (120, 21),
            # (0, 0),
            (1534236469, 0),  # Overflow case
            (-2147483648, 0),  # Overflow case
        ]

    def test_reverse(self):
        for x, expected in self.test_cases:
            result = self.solution.reverse(x)
            self.assertEqual(result, expected)

    def test_reverse_v2(self):
        for x, expected in self.test_cases:
            result = self.solution.reverse_v2(x)
            self.assertEqual(result, expected)

    def test_reverse_v3(self):
        for x, expected in self.test_cases:
            result = self.solution.reverse_v3(x)
            self.assertEqual(result, expected)

    def test_reverse_v4(self):
        for x, expected in self.test_cases:
            result = self.solution.reverse_v4(x)
            self.assertEqual(result, expected)
