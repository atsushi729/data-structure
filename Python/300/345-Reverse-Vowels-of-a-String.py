import unittest


#################### Solution ####################
def reverse_vowels(s: str) -> str:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    match_list = []
    s_list = list(s)
    vowels_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for word in s:
        if word in vowels_list:
            match_list.append(word)

    if len(match_list) == 0:
        return s

    for i in range(len(s_list)):
        if s_list[i] in vowels_list:
            s_list[i] = match_list[-1]
            match_list.pop()

    return "".join(s_list)


#################### Test Case ####################
class TestReverseVowels(unittest.TestCase):
    def test_reverse_vowels(self):
        self.assertEqual(reverse_vowels("hello"), "holle")
        self.assertEqual(reverse_vowels("leetcode"), "leotcede")
        self.assertEqual(reverse_vowels("aA"), "Aa")
