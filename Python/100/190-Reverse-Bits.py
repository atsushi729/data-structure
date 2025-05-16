import unittest


class Solution:
    def reverse_bits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            (43261596, 964176192),
            (4294967293, 3221225471),
            (0, 0),
            (1, 2147483648),
            (2, 1073741824),
            (3, 3221225472),
        ]

    def test_reverse_bits(self):
        for n, expected in self.test_cases:
            result = self.solution.reverse_bits(n)
            self.assertEqual(result, expected)
