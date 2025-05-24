import unittest


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


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            (123, 321),
            (-123, -321),
            (120, 21),
            (0, 0),
            (1534236469, 0),  # Overflow case
            (-2147483648, 0),  # Overflow case
        ]

    def test_reverse(self):
        for x, expected in self.test_cases:
            result = self.solution.reverse(x)
            self.assertEqual(result, expected)
