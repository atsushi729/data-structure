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

    def length_of_longest_substring_v3(self, s: str) -> int:
        char_index = {}
        left = 0
        longest = 0

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right

            longest = max(longest, right - left + 1)
        return longest

    def length_of_longest_substring_v4(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

    def length_of_longest_substring_v5(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        max_len = 0
        list_s = list(s)

        for i, char in enumerate(list_s):
            while char in list_s[l:i]:
                l += 1
            max_len = max(max_len, len(list_s[l:i]))
        return max_len + 1


#################### Test Case ####################
class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

        self.methods = [
            self.solution.length_of_longest_substring,
            self.solution.length_of_longest_substring_v2,
            self.solution.length_of_longest_substring_v3,
            self.solution.length_of_longest_substring_v4,
            self.solution.length_of_longest_substring_v5,
        ]

        self.test_cases = [
            # Standard cases
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),

            # Empty string
            ("", 0),

            # Single character
            ("a", 1),

            # Two unique characters
            ("au", 2),

            # Duplicate character inside the window
            ("dvdf", 3),
            ("abba", 2),
            ("tmmzuxt", 5),

            # Longest substring appears at the end
            ("anviaj", 5),

            # All characters are unique
            ("abcdef", 6),

            # Repeated pattern
            ("abcabc", 3),

            # Whitespace characters
            (" ", 1),
            ("a b c", 3),
            ("  ", 1),

            # Numeric characters
            ("12345123", 5),

            # Case-sensitive characters
            ("aA", 2),
            ("aAaA", 2),

            # Unicode characters
            ("あいうあえ", 4),
        ]

    def test_length_of_longest_substring(self):
        for method in self.methods:
            for s, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        input=s,
                        expected=expected,
                ):
                    result = method(s)
                    self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
