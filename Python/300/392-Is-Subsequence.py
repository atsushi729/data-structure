import unittest


class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        i = 0

        for c in t:
            if len(s) > i and s[i] == c:
                i += 1

        return i == len(s)

    def is_subsequence2(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        for j in range(m + 1):
            dp[n][j] = True

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]
        return dp[0][0]


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

    def test_is_subsequence2(self):
        for s, t, expected in self.test_cases:
            with self.subTest(s=s, t=t):
                self.assertEqual(self.solution.is_subsequence2(s, t), expected)
