import unittest


class Solution:
    def int_to_roman(self, num: int) -> str:
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        vals = dict(sorted(vals.items(), key=lambda x: x[1], reverse=True))
        res = []

        for roman, val in vals.items():
            while num >= val:
                res.append(roman)
                num -= val
        return "".join(res)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_case = [
            (3, "III"),
            (4, "IV"),
            (9, "IX"),
            (58, "LVIII"),
            (1994, "MCMXCIV"),
        ]

    def test_int_to_roman(self):
        for num, expected in self.test_case:
            with self.subTest(num=num):
                self.assertEqual(expected, self.s.int_to_roman(num))
