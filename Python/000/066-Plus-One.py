from typing import List
import unittest


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        result = int("".join(map(str, digits)))
        total = result + 1
        res = []
        for n in str(total):
            res.append(int(n))
        return res

    def plus_one2(self, digits: List[int]) -> List[int]:
        one = 1
        i = 0
        digits.reverse()

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(one)
                one = 0
            i += 1
        digits.reverse()
        return digits


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([1, 2, 3], [1, 2, 4]),
            ([4, 3, 2, 1], [4, 3, 2, 2]),
            ([0], [1]),
            ([9], [1, 0]),
            ([9, 9], [1, 0, 0]),
            ([1, 9, 9], [2, 0, 0]),
            ([9, 9, 9], [1, 0, 0, 0]),
        ]

    def test_plus_one(self):
        for digits, expected in self.test_cases:
            with self.subTest(digits=digits):
                result = self.solution.plus_one(digits)
                self.assertEqual(result, expected)

    def test_plus_one2(self):
        for digits, expected in self.test_cases:
            with self.subTest(digits=digits):
                result = self.solution.plus_one2(digits)
                self.assertEqual(result, expected)
