import unittest


#################### Solution ####################
def length_of_longest_substring(s: str) -> int:
    current_max = 0
    box = []

    for char in s:
        box.append(char)

        if len(list(set(box))) == len(box):
            current_max = max(current_max, len(box))
        else:
            index = box.index(char) + 1
            box = box[index:]

    current_max = max(current_max, len(box))
    return current_max


def length_of_longest_substring_v2(s: str) -> int:
    if not s:
        return 0

    seen = {}
    start = 0
    longest = 0

    for i, c in enumerate(s):
        if c in seen and seen[c] >= start:
            start = seen[c] + 1
        else:
            longest = max(longest, i - start + 1)
        seen[c] = i

    return longest


#################### Test Case ####################
class TestLengthOfLongestSubstring(unittest.TestCase):
    def test_length_of_longest_substring(self):
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)
        self.assertEqual(length_of_longest_substring("bbbbb"), 1)
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)
        self.assertEqual(length_of_longest_substring(""), 0)
        self.assertEqual(length_of_longest_substring(" "), 1)
        self.assertEqual(length_of_longest_substring("au"), 2)
        self.assertEqual(length_of_longest_substring("dvdf"), 3)
        self.assertEqual(length_of_longest_substring("abba"), 2)

    def test_length_of_longest_substring_v2(self):
        self.assertEqual(length_of_longest_substring_v2("abcabcbb"), 3)
        self.assertEqual(length_of_longest_substring_v2("bbbbb"), 1)
        self.assertEqual(length_of_longest_substring_v2("pwwkew"), 3)
        self.assertEqual(length_of_longest_substring_v2(""), 0)
        self.assertEqual(length_of_longest_substring_v2(" "), 1)
        self.assertEqual(length_of_longest_substring_v2("au"), 2)
        self.assertEqual(length_of_longest_substring_v2("dvdf"), 3)
        self.assertEqual(length_of_longest_substring_v2("abba"), 2)
