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

    def numDistinct3(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][len(t)] = 1

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]

    def numDistinct4(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        nextDp = [0] * (n + 1)

        dp[n] = nextDp[n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                nextDp[j] = dp[j]
                if s[i] == t[j]:
                    nextDp[j] += dp[j + 1]
            dp = nextDp[:]

        return dp[0]

    def numDistinct5(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)

        dp[n] = 1
        for i in range(m - 1, -1, -1):
            prev = 1
            for j in range(n - 1, -1, -1):
                res = dp[j]
                if s[i] == t[j]:
                    res += prev

                prev = dp[j]
                dp[j] = res

        return dp[0]


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

    def test_num_distinct3(self):
        for s, t, expected in self.test_cases:
            with self.subTest(s=s, t=t):
                result = self.solution.numDistinct3(s, t)
                self.assertEqual(result, expected, f"Failed for s: {s}, t: {t}. Expected {expected}, got {result}.")

    def test_num_distinct4(self):
        for s, t, expected in self.test_cases:
            with self.subTest(s=s, t=t):
                result = self.solution.numDistinct4(s, t)
                self.assertEqual(result, expected, f"Failed for s: {s}, t: {t}. Expected {expected}, got {result}.")

    def test_num_distinct5(self):
        for s, t, expected in self.test_cases:
            with self.subTest(s=s, t=t):
                result = self.solution.numDistinct5(s, t)
                self.assertEqual(result, expected, f"Failed for s: {s}, t: {t}. Expected {expected}, got {result}.")
