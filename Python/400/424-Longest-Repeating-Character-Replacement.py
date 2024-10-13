import unittest


#################### Solution ####################
def character_replacement(s: str, k: int) -> int:
    count = {}
    max_count = 0
    left = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]
        count[char] = count.get(char, 0) + 1
        max_count = max(max_count, count[char])

        # sliding window condition
        if (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1

        # update the max_length
        max_length = max(max_length, right - left + 1)

    return max_length


#################### Test Case ####################
class TestCharacterReplacement(unittest.TestCase):
    def test_character_replacement(self):
        self.assertEqual(character_replacement("ABAB", 2), 4)
        self.assertEqual(character_replacement("AABABBA", 1), 4)
        self.assertEqual(character_replacement("AABABBA", 0), 2)

