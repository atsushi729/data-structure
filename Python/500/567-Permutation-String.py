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


#################### Test Case ####################
class TestCheckInclusion(unittest.TestCase):
    def test_check_inclusion(self):
        self.assertEqual(check_inclusion("ab", "eidbaooo"), True)
        self.assertEqual(check_inclusion("ab", "eidboaoo"), False)
        self.assertEqual(check_inclusion("adc", "dcda"), True)
