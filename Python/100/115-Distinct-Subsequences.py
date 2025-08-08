import unittest


class Solution:
    def num_distinct(self, s: str, t: str) -> int:
        """
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
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

    def num_distinct2(self, s: str, t: str) -> int:
        """
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
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

    def num_distinct3(self, s: str, t: str) -> int:
        """
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
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

    def num_distinct4(self, s: str, t: str) -> int:
        """
        Time Complexity: O(m * n)
        Space Complexity: O(n)
        """
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

    def num_distinct5(self, s: str, t: str) -> int:
        """
        Time Complexity: O(m * n)
        Space Complexity: O(n)
        """
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

    def num_distinct6(self, s: str, t: str) -> int:
        """
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        if len(t) > len(s):
            return 0

        dp = {}

        def dfs(i, j):
            print(f"Entering dfs(i={i}, j={j})")

            if j == len(t):
                print(f"✔️ t matched completely at i={i}, j={j} → return 1")
                return 1
            if i == len(s):
                print(f"❌ s exhausted at i={i}, j={j} → return 0")
                return 0
            if (i, j) in dp:
                print(f"🔁 Returning memoized dp[{i},{j}] = {dp[(i, j)]}")
                return dp[(i, j)]

            print(f"Trying to skip s[{i}]='{s[i]}' and keep t[{j}]='{t[j]}'")
            res = dfs(i + 1, j)

            if s[i] == t[j]:
                print(f"✅ s[{i}]='{s[i]}' matches t[{j}]='{t[j]}', trying to match the rest")
                res += dfs(i + 1, j + 1)
            else:
                print(f"🚫 s[{i}]='{s[i]}' does NOT match t[{j}]='{t[j]}'")

            dp[(i, j)] = res
            print(f"↩️ dp[{i},{j}] = {res} (returning)")
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
                result = self.solution.num_distinct(s, t)
                self.assertEqual(result, expected, f"Failed for s: {s}, t: {t}. Expected {expected}, got {result}.")

    def test_num_distinct2(self):
        for s, t, expected in self.test_cases:
            with self.subTest(s=s, t=t):
                result = self.solution.num_distinct2(s, t)
                self.assertEqual(result, expected, f"Failed for s: {s}, t: {t}. Expected {expected}, got {result}.")

    def test_num_distinct3(self):
        for s, t, expected in self.test_cases:
            with self.subTest(s=s, t=t):
                result = self.solution.num_distinct3(s, t)
                self.assertEqual(result, expected, f"Failed for s: {s}, t: {t}. Expected {expected}, got {result}.")

    def test_num_distinct4(self):
        for s, t, expected in self.test_cases:
            with self.subTest(s=s, t=t):
                result = self.solution.num_distinct4(s, t)
                self.assertEqual(result, expected, f"Failed for s: {s}, t: {t}. Expected {expected}, got {result}.")

    def test_num_distinct5(self):
        for s, t, expected in self.test_cases:
            with self.subTest(s=s, t=t):
                result = self.solution.num_distinct5(s, t)
                self.assertEqual(result, expected, f"Failed for s: {s}, t: {t}. Expected {expected}, got {result}.")

    def test_num_distinct6(self):
        for s, t, expected in self.test_cases:
            with self.subTest(s=s, t=t):
                result = self.solution.num_distinct6(s, t)
                self.assertEqual(result, expected, f"Failed for s: {s}, t: {t}. Expected {expected}, got {result}.")
