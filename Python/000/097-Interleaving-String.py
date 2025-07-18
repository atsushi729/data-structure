import unittest


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
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

    def test_isInterleave(self):
        for s1, s2, s3, expected in self.test_cases:
            with self.subTest(s1=s1, s2=s2, s3=s3):
                result = self.solution.isInterleave(s1, s2, s3)
                self.assertEqual(result, expected)