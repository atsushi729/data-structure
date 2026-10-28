import unittest


class Solution:
    def reverse_bits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res

    def reverse_bits_v2(self, n: int) -> int:
        binary = ""

        for i in range(32):
            if n & (1 << i):
                binary += "1"
            else:
                binary += "0"

        res = 0

        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                res |= (1 << i)
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.methods = [
            cls.solution.reverse_bits,
            cls.solution.reverse_bits_v2,
        ]

        cls.test_cases = [
            (43261596, 964176192),
            (4294967293, 3221225471),
            (0, 0),
            (1, 2147483648),
            (2, 1073741824),
            (3, 3221225472),
            (4294967295, 4294967295),
            (2147483648, 1),
        ]

    def test_reverse_bits(self):
        for method in self.methods:
            for n, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        n=n,
                ):
                    result = method(n)
                    self.assertEqual(result, expected)
