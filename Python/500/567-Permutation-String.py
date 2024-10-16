import unittest


#################### Solution ####################
def check_inclusion(s1: str, s2: str) -> bool:
    if len(s2) < len(s1):
        return False

    sorted_s1 = sorted(s1)

    for i in range(len(s2) - len(s1) + 1):
        target_char = s2[i:len(s1) + i]
        sorted_target = sorted(target_char)

        if sorted_target == sorted_s1:
            return True

    return False


def model_check_inclusion(s1: str, s2: str) -> bool:
    if len(s2) < len(s1):
        return False

    s1_map = {}
    s2_map = {}
    for i in range(26):
        s1_map[chr(97 + i)] = 0
        s2_map[chr(97 + i)] = 0

    for i in range(len(s1)):
        s1_map[s1[i]] += 1
        s2_map[s2[i]] += 1

    if s1_map == s2_map:
        return True

    for i in range(len(s1), len(s2)):
        s2_map[s2[i]] += 1
        s2_map[s2[i - len(s1)]] -= 1

        if s1_map == s2_map:
            return True

    return False


#################### Test Case ####################
class TestCheckInclusion(unittest.TestCase):
    def test_check_inclusion(self):
        self.assertEqual(check_inclusion("ab", "eidbaooo"), True)
        self.assertEqual(check_inclusion("ab", "eidboaoo"), False)
        self.assertEqual(check_inclusion("adc", "dcda"), True)

    def test_model_check_inclusion(self):
        self.assertEqual(model_check_inclusion("ab", "eidbaooo"), True)
        self.assertEqual(model_check_inclusion("ab", "eidboaoo"), False)
        self.assertEqual(model_check_inclusion("adc", "dcda"), True)
