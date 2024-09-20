import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = sorted(list(s))
        t_list = sorted(list(t))

        if s_list == t_list:
            return True
        else:
            return False

    ## another solution
    def isAnagram2(self, y, t):
        # Check if the two strings have the same length
        if len(y) != len(t):
            return False

        # Create a frequency table for string s
        freq = {}
        for char in y:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # Check if the characters in string t are in the frequency table
        for char in t:
            if char in freq and freq[char] > 0:
                freq[char] -= 1
            else:
                return False

        return True


class TestIsAnagram(unittest.TestCase):
    def test_isAnagram(self):
        self.assertEqual(Solution().isAnagram("anagram", "nagaram"), True)
        self.assertEqual(Solution().isAnagram("rat", "car"), False)
        self.assertEqual(Solution().isAnagram("a", "ab"), False)
        self.assertEqual(Solution().isAnagram("ab", "a"), False)
        self.assertEqueal(Solution().isAnagram("abcabc", "abcabc"), True)


if __name__ == '__main__':
    y = "anagram"
    t = "nagaram"
    s = Solution()
    print(s.isAnagram2(y, t))
