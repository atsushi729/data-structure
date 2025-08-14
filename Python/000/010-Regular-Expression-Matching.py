import unittest


class Solution:
    def is_match(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        cache = {}

        def dfs(i, j):
            if j == n:
                return i == m
            if (i, j) in cache:
                return cache[(i, j)]

            match = i < m and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < n and p[j + 1] == "*":
                cache[(i, j)] = (dfs(i, j + 2) or
                                 (match and dfs(i + 1, j)))
                return cache[(i, j)]

            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return False

        return dfs(0, 0)

    def is_match2(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def dfs(i, j):
            if j == n:
                return i == m

            match = i < m and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < n and p[j + 1] == "*":
                return (dfs(i, j + 2) or  # don't use *
                        (match and dfs(i + 1, j)))  # use *
            if match:
                return dfs(i + 1, j + 1)
            return False

        return dfs(0, 0)

    def is_match3(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        dp[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                if (j + 1) < len(p) and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2]
                    if match:
                        dp[i][j] = dp[i + 1][j] or dp[i][j]
                elif match:
                    dp[i][j] = dp[i + 1][j + 1]

        return dp[0][0]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("aa", "a", False),
            ("aa", "a*", True),
            ("ab", ".*", True),
            ("aab", "c*a*b", True),
            ("mississippi", "mis*is*p*.", False),
            ("", ".*", True),
            ("", "", True),
            ("a", "", False),
            ("a*", "", False),
            ("ab", ".*c", False)
        ]

    def test_is_match(self):
        for s, p, expected in self.test_cases:
            with self.subTest(s=s, p=p):
                self.assertEqual(self.solution.is_match(s, p), expected)

    def test_is_match2(self):
        for s, p, expected in self.test_cases:
            with self.subTest(s=s, p=p):
                self.assertEqual(self.solution.is_match2(s, p), expected)

    def test_is_match3(self):
        for s, p, expected in self.test_cases:
            with self.subTest(s=s, p=p):
                self.assertEqual(self.solution.is_match3(s, p), expected)
