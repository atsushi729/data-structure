import unittest


class Solution:
    def is_interleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def dfs(i, j, k):
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))
            if (i, j) in dp:
                return dp[(i, j)]

            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1)
            if not res and j < len(s2) and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)

            dp[(i, j)] = res
            return res

        return dfs(0, 0, 0)

    def is_interleave2(self, s1: str, s2: str, s3: str) -> bool:

        def dfs(i, j, k):
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))

            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j, k + 1):
                    return True

            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1):
                    return True

            return False

        return dfs(0, 0, 0)

    def is_inter_leave_3(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]

    def is_interleave4(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        if n < m:
            s1, s2 = s2, s1
            m, n = n, m

        dp = [False for _ in range(n + 1)]
        dp[n] = True
        for i in range(m, -1, -1):
            nextDp = [False for _ in range(n + 1)]
            nextDp[n] = True
            for j in range(n, -1, -1):
                if i < m and s1[i] == s3[i + j] and dp[j]:
                    nextDp[j] = True
                if j < n and s2[j] == s3[i + j] and nextDp[j + 1]:
                    nextDp[j] = True
            dp = nextDp
        return dp[0]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("aabcc", "dbbca", "aadbbcbcac", True),
            ("aabcc", "dbbca", "aadbbbaccc", False),
            ("", "", "", True),
            ("a", "", "a", True),
            ("", "b", "b", True),
            ("abc", "def", "abcdef", True),
            ("abc", "def", "abdecf", True)
        ]

    def test_is_interleave(self):
        for s1, s2, s3, expected in self.test_cases:
            with self.subTest(s1=s1, s2=s2, s3=s3):
                result = self.solution.is_interleave(s1, s2, s3)
                self.assertEqual(result, expected)

    def test_is_interleave2(self):
        for s1, s2, s3, expected in self.test_cases:
            with self.subTest(s1=s1, s2=s2, s3=s3):
                result = self.solution.is_interleave2(s1, s2, s3)
                self.assertEqual(result, expected)

    def test_is_interleave3(self):
        for s1, s2, s3, expected in self.test_cases:
            with self.subTest(s1=s1, s2=s2, s3=s3):
                result = self.solution.is_inter_leave_3(s1, s2, s3)
                self.assertEqual(result, expected)

    def test_is_interleave4(self):
        for s1, s2, s3, expected in self.test_cases:
            with self.subTest(s1=s1, s2=s2, s3=s3):
                result = self.solution.is_interleave4(s1, s2, s3)
                self.assertEqual(result, expected)
