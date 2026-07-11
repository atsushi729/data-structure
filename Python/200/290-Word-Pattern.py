import unittest


class Solution:
    def word_pattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        chat_to_word = {}
        store = set()

        for i, (c, w) in enumerate(zip(pattern, words)):
            if c in chat_to_word:
                if words[chat_to_word[c]] != w:
                    return False
            else:
                if w in store:
                    return False
                chat_to_word[c] = i
                store.add(w)
        return True


class TestSolution(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("abba", "dog cat cat dog", True),
            ("abba", "dog cat cat fish", False),
        ]

    def test_word_pattern(self):
        for pattern, s, expected in self.test_cases:
            with self.subTest(pattern=pattern, s=s):
                self.assertEqual(self.solution.word_pattern(pattern, s), expected)
