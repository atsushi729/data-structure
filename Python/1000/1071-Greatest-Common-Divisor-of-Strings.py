import math
import unittest


def gcdOfStrings(self, str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    return str1[:math.gcd(len(str1), len(str2))]


class TestGcdOfStrings(unittest.TestCase):
    def test_gcd_of_strings(self):
        self.assertEqual(gcdOfStrings(self, "ABCABC", "ABC"), "ABC")
        self.assertEqual(gcdOfStrings(self, "ABABAB", "ABAB"), "AB")
        self.assertEqual(gcdOfStrings(self, "LEET", "CODE"), "")
