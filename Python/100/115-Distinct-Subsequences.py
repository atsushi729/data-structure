import unittest


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            dp[(i, j)] = res
            return res

        return dfs(0, 0)

    def numDistinct2(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            return res

        return dfs(0, 0)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("rabbbit", "rabbit", 3),
            ("babgbag", "bag", 5),
            ("a", "a", 1),
            ("a", "b", 0),
            ("", "", 1),
            ("abc", "", 1),
            ("", "abc", 0)
        ]

    def test_num_distinct(self):
        for s, t, expected in self.test_cases:
            with self.subTest(s=s, t=t):
                result = self.solution.numDistinct(s, t)
                self.assertEqual(result, expected, f"Failed for s: {s}, t: {t}. Expected {expected}, got {result}.")

    def test_num_distinct2(self):
        for s, t, expected in self.test_cases:
            with self.subTest(s=s, t=t):
                result = self.solution.numDistinct2(s, t)
                self.assertEqual(result, expected, f"Failed for s: {s}, t: {t}. Expected {expected}, got {result}.")
