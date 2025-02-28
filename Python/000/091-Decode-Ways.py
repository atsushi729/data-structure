import unittest


class Solution:
    def num_decodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)

            if i + 1 < len(s) and (
                    s[i] == "1" or s[i] == "2" and
                    s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)

            dp[i] = res
            return res

        return dfs(0)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_num_decodings(self):
        self.assertEqual(self.sol.num_decodings("12"), 2)
        self.assertEqual(self.sol.num_decodings("226"), 3)
        self.assertEqual(self.sol.num_decodings("0"), 0)
        self.assertEqual(self.sol.num_decodings("06"), 0)
        self.assertEqual(self.sol.num_decodings("10"), 1)
        self.assertEqual(self.sol.num_decodings("101"), 1)
