import unittest


class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        word1_list = list(word1)
        word2_list = list(word2)
        res = []

        while word1_list and word2_list:
            res.append(word1_list.pop(0))
            res.append(word2_list.pop(0))

        if word1_list:
            res.extend(word1_list)
        if word2_list:
            res.extend(word2_list)

        return "".join(res)

    def merge_alternately_v2(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)

    def merge_alternately_v3(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        res = []
        for i in range(max(n, m)):
            if i < n:
                res.append(word1[i])
            if i < m:
                res.append(word2[i])
        return "".join(res)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            ("abc", "pqr", "apbqcr"),
            ("ab", "pqrs", "apbqrs"),
            ("abcd", "pq", "apbqcd"),
            ("", "xyz", "xyz"),
            ("hello", "", "hello"),
            ("a", "b", "ab"),
        ]

    def test_merge_alternately(self):
        for word1, word2, expected in self.test_cases:
            with self.subTest(word1=word1, word2=word2, expected=expected):
                self.assertEqual(self.s.merge_alternately(word1, word2), expected)

    def test_merge_alternately_v2(self):
        for word1, word2, expected in self.test_cases:
            with self.subTest(word1=word1, word2=word2, expected=expected):
                self.assertEqual(self.s.merge_alternately_v2(word1, word2), expected)

    def test_merge_alternately_v3(self):
        for word1, word2, expected in self.test_cases:
            with self.subTest(word1=word1, word2=word2, expected=expected):
                self.assertEqual(self.s.merge_alternately_v3(word1, word2), expected)
