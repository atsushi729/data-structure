import unittest


#################### Solution ####################
def reverse_words(s: str) -> str:
    return " ".join(s.split()[::-1])


#################### Test Case ####################
class TestReverseWords(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual(reverse_words("the sky is blue"), "blue is sky the")
        self.assertEqual(reverse_words("  hello world  "), "world hello")
        self.assertEqual(reverse_words("a good   example"), "example good a")
