import unittest


class Solution:
    def longest_common_subsequence(self, text1: str, text2: str) -> int:

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)
            return max(dfs(i + 1, j), dfs(i, j + 1))

        return dfs(0, 0)

    def longest_common_subsequence_v2(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))

            return memo[(i, j)]

        return dfs(0, 0)

    def longest_common_subsequence_v3(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]

    def longest_common_subsequence_v4(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        prev = [0] * (len(text2) + 1)
        curr = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(curr[j + 1], prev[j])
            prev, curr = curr, prev

        return prev[0]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_longest_common_subsequence(self):
        self.assertEqual(self.solution.longest_common_subsequence("abcde", "ace"), 3)
        self.assertEqual(self.solution.longest_common_subsequence("abc", "abc"), 3)
        self.assertEqual(self.solution.longest_common_subsequence("abc", "def"), 0)
        self.assertEqual(self.solution.longest_common_subsequence("", ""), 0)
        self.assertEqual(self.solution.longest_common_subsequence("a", "a"), 1)

    def test_longest_common_subsequence_v2(self):
        self.assertEqual(self.solution.longest_common_subsequence_v2("abcde", "ace"), 3)
        self.assertEqual(self.solution.longest_common_subsequence_v2("abc", "abc"), 3)
        self.assertEqual(self.solution.longest_common_subsequence_v2("abc", "def"), 0)
        self.assertEqual(self.solution.longest_common_subsequence_v2("", ""), 0)
        self.assertEqual(self.solution.longest_common_subsequence_v2("a", "a"), 1)

    def test_longest_common_subsequence_v3(self):
        self.assertEqual(self.solution.longest_common_subsequence_v3("abcde", "ace"), 3)
        self.assertEqual(self.solution.longest_common_subsequence_v3("abc", "abc"), 3)
        self.assertEqual(self.solution.longest_common_subsequence_v3("abc", "def"), 0)
        self.assertEqual(self.solution.longest_common_subsequence_v3("", ""), 0)
        self.assertEqual(self.solution.longest_common_subsequence_v3("a", "a"), 1)

    def test_longest_common_subsequence_v4(self):
        self.assertEqual(self.solution.longest_common_subsequence_v4("abcde", "ace"), 3)
        self.assertEqual(self.solution.longest_common_subsequence_v4("abc", "abc"), 3)
        self.assertEqual(self.solution.longest_common_subsequence_v4("abc", "def"), 0)
        self.assertEqual(self.solution.longest_common_subsequence_v4("", ""), 0)
        self.assertEqual(self.solution.longest_common_subsequence_v4("a", "a"), 1)