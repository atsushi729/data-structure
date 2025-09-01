import unittest


#################### Solution ####################
class Solution:
    def length_of_longest_substring(self, s: str) -> int:
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

    def length_of_longest_substring_v2(self, s: str) -> int:
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
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
            ("", 0),
            ("au", 2),
            ("dvdf", 3),
            ("anviaj", 5),
        ]

    def test_length_of_longest_substring(self):
        for s, expected in self.test_cases:
            with self.subTest(s=s):
                result = self.solution.length_of_longest_substring(s)
                self.assertEqual(result, expected)

    def test_length_of_longest_substring_v2(self):
        for s, expected in self.test_cases:
            with self.subTest(s=s):
                result = self.solution.length_of_longest_substring_v2(s)
                self.assertEqual(result, expected)
