import unittest


class Solution:
    def get_sum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= max_int else ~(a ^ mask)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            (1, 2, 3),
            (-2, 3, 1),
            (0, 0, 0),
            (-1, -1, -2),
            (5, -3, 2),
            (-5, 3, -2),
        ]

    def test_get_sum(self):
        for a, b, expected in self.test_cases:
            result = self.solution.get_sum(a, b)
            self.assertEqual(result, expected)
