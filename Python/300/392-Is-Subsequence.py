import unittest


class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        i = 0

        for c in t:
            if len(s) > i and s[i] == c:
                i += 1

        return i == len(s)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("abc", "ahbgdc", True),
            ("axc", "ahbgdc", False),
        ]

    def test_is_subsequence(self):
        for s, t, expected in self.test_cases:
            with self.subTest(s=s, t=t):
                self.assertEqual(self.solution.is_subsequence(s, t), expected)
