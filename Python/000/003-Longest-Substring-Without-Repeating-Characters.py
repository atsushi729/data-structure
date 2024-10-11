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
