from typing import List
import unittest


class Solution:
    def count_bits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            one = 0
            for i in range(32):
                if num & (1 << i):
                    one += 1
            res.append(one)
        return res

    def count_bits_v2(self, n: int) -> List[int]:
        ans_list = []

        for i in range(n + 1):
            res = self.count_bit(i)
            ans_list.append(res)
        return ans_list

    def count_bit(self, nums: int):
        res = 0

        while nums:
            res += nums % 2
            nums = nums >> 1
        return res

    def count_bits_v3(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            num = i
            while num != 0:
                res[i] += 1
                num &= (num - 1)
        return res

    def count_bits_v4(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n + 1)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            (2, [0, 1, 1]),
            (5, [0, 1, 1, 2, 1, 2]),
            (0, [0]),
            (7, [0, 1, 1, 2, 1, 2, 2, 3]),
            (10, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]),
        ]

    def test_count_bits(self):
        for n, expected in self.test_cases:
            result = self.solution.count_bits(n)
            self.assertEqual(result, expected)

    def test_count_bits_v2(self):
        for n, expected in self.test_cases:
            result = self.solution.count_bits_v2(n)
            self.assertEqual(result, expected)

    def test_count_bits_v3(self):
        for n, expected in self.test_cases:
            result = self.solution.count_bits_v3(n)
            self.assertEqual(result, expected)

    def test_count_bits_v4(self):
        for n, expected in self.test_cases:
            result = self.solution.count_bits_v4(n)
            self.assertEqual(result, expected)
