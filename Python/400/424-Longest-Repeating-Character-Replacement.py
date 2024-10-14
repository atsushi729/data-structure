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


def model_character_replacement(s: str, k: int) -> int:
    count = {}
    l = 0
    maxf = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1

    return (r - l + 1)


#################### Test Case ####################
class TestCharacterReplacement(unittest.TestCase):
    def test_character_replacement(self):
        self.assertEqual(character_replacement("ABAB", 2), 4)
        self.assertEqual(character_replacement("AABABBA", 1), 4)
        self.assertEqual(character_replacement("AABABBA", 0), 2)

    def test_model_character_replacement(self):
        self.assertEqual(model_character_replacement("ABAB", 2), 4)
        self.assertEqual(model_character_replacement("AABABBA", 1), 4)
        self.assertEqual(model_character_replacement("AABABBA", 0), 2)
