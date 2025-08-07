import unittest


class Solution:
    def min_distance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]

    def min_distance2(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            res = min(dfs(i + 1, j), dfs(i, j + 1))
            res = min(res, dfs(i + 1, j + 1))
            return res + 1

        return dfs(0, 0)

    def min_distance3(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = {}

        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                res = min(dfs(i + 1, j), dfs(i, j + 1))
                res = min(res, dfs(i + 1, j + 1))
                dp[(i, j)] = res + 1
            return dp[(i, j)]

        return dfs(0, 0)

    def min_distance4(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1

        dp = [0] * (n + 1)
        nextDp = [0] * (n + 1)

        for j in range(n + 1):
            dp[j] = n - j

        for i in range(m - 1, -1, -1):
            nextDp[n] = m - i
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    nextDp[j] = dp[j + 1]
                else:
                    nextDp[j] = 1 + min(dp[j], nextDp[j + 1], dp[j + 1])
            dp = nextDp[:]

        return dp[0]

    def min_distance5(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1

        dp = [n - i for i in range(n + 1)]

        for i in range(m - 1, -1, -1):
            nextDp = dp[n]
            dp[n] = m - i
            for j in range(n - 1, -1, -1):
                temp = dp[j]
                if word1[i] == word2[j]:
                    dp[j] = nextDp
                else:
                    dp[j] = 1 + min(dp[j], dp[j + 1], nextDp)
                nextDp = temp
        return dp[0]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("horse", "ros", 3),
            ("intention", "execution", 5),
            ("", "", 0),
            ("a", "b", 1),
            ("abc", "yabd", 2),
        ]

    def test_min_distance(self):
        for word1, word2, expected in self.test_cases:
            with self.subTest(word1=word1, word2=word2):
                result = self.solution.min_distance(word1, word2)
                self.assertEqual(result, expected, f"Failed for {word1} and {word2}")

    def test_min_distance2(self):
        for word1, word2, expected in self.test_cases:
            with self.subTest(word1=word1, word2=word2):
                result = self.solution.min_distance2(word1, word2)
                self.assertEqual(result, expected, f"Failed for {word1} and {word2}")

    def test_min_distance3(self):
        for word1, word2, expected in self.test_cases:
            with self.subTest(word1=word1, word2=word2):
                result = self.solution.min_distance3(word1, word2)
                self.assertEqual(result, expected, f"Failed for {word1} and {word2}")

    def test_min_distance4(self):
        for word1, word2, expected in self.test_cases:
            with self.subTest(word1=word1, word2=word2):
                result = self.solution.min_distance4(word1, word2)
                self.assertEqual(result, expected, f"Failed for {word1} and {word2}")

    def test_min_distance5(self):
        for word1, word2, expected in self.test_cases:
            with self.subTest(word1=word1, word2=word2):
                result = self.solution.min_distance5(word1, word2)
                self.assertEqual(result, expected, f"Failed for {word1} and {word2}")
