import unittest


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.s = Solution()
        cls.test_case = [
            ("Base case: True", "anagram", "nagaram", True),
            ("Base case: False", "nagaram", "nagaram", False),
            ("Base case: True", "nagaram", "nagaram", True),
        ]

    def test_is_anagram(self):
        for name, s, t, expected in self.test_case:
            with self.subTest(name=name):
                self.assertTrue(self.s.is_anagram(s, t), expected)
