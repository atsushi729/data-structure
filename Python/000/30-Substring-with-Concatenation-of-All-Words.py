import unittest
from collections import defaultdict, Counter


class Solution:
    def find_substring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        need = Counter(words)
        res = []

        for offset in range(word_len):
            left = offset
            seen = defaultdict(int)
            count = 0

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in need:
                    seen[word] += 1
                    count += 1

                    while seen[word] > need[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                    if count == word_count:
                        res.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = right + word_len
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
            ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], [])
        ]

    def test_find_substring(self):
        for s, words, expected in self.test_cases:
            with self.subTest(s=s, words=words):
                self.assertEqual(expected, self.solution.find_substring(s, words))
