import unittest


#################### Solution ####################
def reverse_words(s: str) -> str:
    return " ".join(s.split()[::-1])


def reverse_words_v2(s: str) -> str:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    s_list = s.split()
    left, right = 0, len(s_list) - 1

    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1

    return " ".join(s_list)


#################### Test Case ####################
class TestReverseWords(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual(reverse_words("the sky is blue"), "blue is sky the")
        self.assertEqual(reverse_words("  hello world  "), "world hello")
        self.assertEqual(reverse_words("a good   example"), "example good a")

    def test_reverse_words_v2(self):
        self.assertEqual(reverse_words_v2("the sky is blue"), "blue is sky the")
        self.assertEqual(reverse_words_v2("  hello world  "), "world hello")
        self.assertEqual(reverse_words_v2("a good   example"), "example good a")