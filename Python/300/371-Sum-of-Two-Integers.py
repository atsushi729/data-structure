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

    def get_sum_v2(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            cur_bit = a_bit ^ b_bit ^ carry
            carry = a_bit + b_bit + carry > 1

            if cur_bit:
                res |= (1 << i)

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        return res


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

    def test_get_sum_v2(self):
        for a, b, expected in self.test_cases:
            result = self.solution.get_sum_v2(a, b)
            self.assertEqual(result, expected)
