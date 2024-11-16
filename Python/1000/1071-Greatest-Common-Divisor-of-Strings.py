import math
import unittest


def gcd_of_strings(self, str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    return str1[:math.gcd(len(str1), len(str2))]


class TestGcdOfStrings(unittest.TestCase):
    def test_gcd_of_strings(self):
        self.assertEqual(gcd_of_strings(self, "ABCABC", "ABC"), "ABC")
        self.assertEqual(gcd_of_strings(self, "ABABAB", "ABAB"), "AB")
        self.assertEqual(gcd_of_strings(self, "LEET", "CODE"), "")
