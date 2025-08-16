import unittest
from typing import List, Tuple


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

    def is_match4(self, s: str, p: str) -> bool:
        tokens: List[Tuple[str, bool]] = []
        i = 0

        while i < len(p):
            ch = p[i]
            if i + 1 < len(p) and p[i + 1] == '*':
                tokens.append((ch, True))
                i += 2
            else:
                tokens.append((ch, False))
                i += 1

        m, T = len(s), len(tokens)

        dp = [False] * (T + 1)
        dp[0] = True

        for j in range(1, T + 1):
            ch, star = tokens[j - 1]
            if star:
                dp[j] = dp[j - 1]
            else:
                dp[j] = False

        for i in range(1, m + 1):
            new = [False] * (T + 1)
            for j in range(1, T + 1):
                ch, star = tokens[j - 1]
                if not star:
                    new[j] = dp[j - 1] and (ch == s[i - 1] or ch == '.')
                else:
                    use_zero = new[j - 1]
                    use_more = dp[j] and (ch == s[i - 1] or ch == '.')
                    new[j] = use_zero or use_more
            dp = new

        return dp[T]


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

    def test_is_match4(self):
        for s, p, expected in self.test_cases:
            with self.subTest(s=s, p=p):
                self.assertEqual(self.solution.is_match4(s, p), expected)
