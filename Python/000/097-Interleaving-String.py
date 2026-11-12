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

        if m < n:
            s1, s2 = s2, s1
            m, n = n, m

        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(m, -1, -1):
            next_dp = [False] * (n + 1)

            for j in range(n, -1, -1):
                if i == m and j == n:
                    next_dp[j] = True
                    continue

                if i < m and s1[i] == s3[i + j] and dp[j]:
                    next_dp[j] = True

                if j < n and s2[j] == s3[i + j] and next_dp[j + 1]:
                    next_dp[j] = True

            dp = next_dp

        return dp[0]

    def is_interleave5(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        if m < n:
            s1, s2 = s2, s1
            m, n = n, m

        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(m, -1, -1):
            if i < m:
                dp[n] = s1[i] == s3[i + n] and dp[n]

            for j in range(n - 1, -1, -1):
                dp[j] = (
                        (i < m and s1[i] == s3[i + j] and dp[j])
                        or
                        (s2[j] == s3[i + j] and dp[j + 1])
                )

        return dp[0]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

        cls.methods = [
            cls.solution.is_interleave,
            cls.solution.is_interleave2,
            cls.solution.is_inter_leave_3,
            cls.solution.is_interleave4,
            cls.solution.is_interleave5,
        ]

        cls.test_cases = [
            # Basic cases
            ("aabcc", "dbbca", "aadbbcbcac", True),
            ("aabcc", "dbbca", "aadbbbaccc", False),
            ("abc", "def", "abcdef", True),
            ("abc", "def", "abdecf", True),
            ("abc", "def", "adbcef", True),
            ("abc", "def", "abdfec", False),

            # Empty strings
            ("", "", "", True),
            ("a", "", "a", True),
            ("", "b", "b", True),
            ("", "abc", "abc", True),
            ("abc", "", "abc", True),
            ("", "abc", "ab", False),

            # Single characters
            ("a", "b", "ab", True),
            ("a", "b", "ba", True),
            ("a", "b", "aa", False),
            ("a", "a", "aa", True),

            # Length mismatch
            ("abc", "def", "abc", False),
            ("abc", "def", "abcdefg", False),
            ("", "", "a", False),

            # Repeated characters
            ("aaa", "aaa", "aaaaaa", True),
            ("aaa", "aaa", "aaaaab", False),
            ("aa", "ab", "aaba", True),

            # Order preservation
            ("abc", "def", "adbecf", True),
            ("abc", "def", "defabc", True),
            ("abc", "def", "acbdef", False),
            ("abc", "def", "abcfed", False),

            # Unequal lengths
            ("a", "bcde", "abcde", True),
            ("abcd", "e", "abcde", True),
            ("a", "bcde", "bcdea", True),

            # DP boundary cases
            ("a", "b", "ba", True),
            ("ab", "cd", "acbd", True),
            ("ab", "cd", "cdab", True),
            ("ab", "cd", "abcd", True),
        ]

    def test_all_methods(self):
        for method in self.methods:
            for s1, s2, s3, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        s1=s1,
                        s2=s2,
                        s3=s3,
                ):
                    result = method(s1, s2, s3)
                    self.assertEqual(result, expected)
