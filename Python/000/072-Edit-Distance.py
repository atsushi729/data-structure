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
