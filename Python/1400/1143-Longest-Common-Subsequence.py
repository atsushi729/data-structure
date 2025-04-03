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
