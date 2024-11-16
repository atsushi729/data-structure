import math
import unittest


#################### Solution ####################
def gcd_of_strings(self, str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    return str1[:math.gcd(len(str1), len(str2))]


def gcd_of_strings_v2(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""

    gcd_length = math.gcd(len(str1), len(str2))

    candidate_str = str1[:gcd_length]

    if candidate_str * (len(str1) // gcd_length) == str1 and candidate_str * (len(str2) // gcd_length) == str2:
        return candidate_str
    else:
        return ""


#################### Test Case ####################
class TestGcdOfStrings(unittest.TestCase):
    def test_gcd_of_strings(self):
        self.assertEqual(gcd_of_strings(self, "ABCABC", "ABC"), "ABC")
        self.assertEqual(gcd_of_strings(self, "ABABAB", "ABAB"), "AB")
        self.assertEqual(gcd_of_strings(self, "LEET", "CODE"), "")

    def test_gcd_of_strings_v2(self):
        self.assertEqual(gcd_of_strings_v2("ABCABC", "ABC"), "ABC")
        self.assertEqual(gcd_of_strings_v2("ABABAB", "ABAB"), "AB")
        self.assertEqual(gcd_of_strings_v2("LEET", "CODE"), "")
