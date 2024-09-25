import unittest


#################### Solution ####################
def is_anagram(s: str, t: str) -> bool:
    s_list = sorted(list(s))
    t_list = sorted(list(t))

    if s_list == t_list:
        return True
    else:
        return False


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
    def test_isAnagram(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True)
        self.assertEqual(is_anagram("rat", "car"), False)
        self.assertEqual(is_anagram("a", "ab"), False)
        self.assertEqual(is_anagram("ab", "a"), False)
        self.assertEqueal(is_anagram("abcabc", "abcabc"), True)
