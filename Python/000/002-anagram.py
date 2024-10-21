import unittest


#################### Solution ####################
def is_anagram(s: str, t: str) -> bool:
    s_list = sorted(list(s))
    t_list = sorted(list(t))

    if s_list == t_list:
        return True
    else:
        return False
    # or simply return s_list == t_list
    # for readability, I used if-else statement.


# Another solution
def is_anagram2(y, t):
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


#################### Test Case ####################
class TestIsAnagram(unittest.TestCase):
    def test_is_anagram(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True)
        self.assertEqual(is_anagram("rat", "car"), False)
        self.assertEqual(is_anagram("a", "ab"), False)
        self.assertEqual(is_anagram("ab", "a"), False)
        self.assertEqueal(is_anagram("abcabc", "abcabc"), True)

    def test_is_anagram2(self):
        self.assertEqual(is_anagram2("anagram", "nagaram"), True)
        self.assertEqual(is_anagram2("rat", "car"), False)
        self.assertEqual(is_anagram2("a", "ab"), False)
        self.assertEqual(is_anagram2("ab", "a"), False)
        self.assertEqueal(is_anagram2("abcabc", "abcabc"), True)
