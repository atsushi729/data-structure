import unittest


class Solution:
    def roman_to_int(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res = 0

        for i in range(len(s)):
            current = values[s[i]]

            if i + 1 < len(s) and current < values[s[i + 1]]:
                res -= current
            else:
                res += current

        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("III", 3),
            ("IV", 4),
            ("IX", 9),
            ("LVIII", 58),
            ("MCMXCIV", 1994),
        ]

    def test_roman_to_int(self):
        for s, expected in self.test_cases:
            with self.subTest(s=s, expected=expected):
                self.assertEqual(
                    self.solution.roman_to_int(s),
                    expected
                )


if __name__ == "__main__":
    unittest.main()
