from typing import List
import unittest


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(i):
            if i == len(s):
                return True

            for w in wordDict:
                if ((i + len(w)) <= len(s) and
                        s[i: i + len(w)] == w
                ):
                    if dfs(i + len(w)):
                        return True
            return False

        return dfs(0)

    def wordBreak_v2(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        def dfs(i):
            if i == len(s):
                return True
            for j in range(i, len(s)):
                if s[i: j + 1] in word_set:
                    if dfs(j + 1):
                        return True
            return False

        return dfs(0)

    def wordBreak_v3(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j: i] in word_set:
                    dp[i] = True
                    break

        return dp[-1]


class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_wordBreak(self):
        self.assertTrue(self.sol.wordBreak("leetcode", ["leet", "code"]))
        self.assertTrue(self.sol.wordBreak("applepenapple", ["apple", "pen"]))
        self.assertFalse(self.sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_wordBreak_v2(self):
        self.assertTrue(self.sol.wordBreak_v2("leetcode", ["leet", "code"]))
        self.assertTrue(self.sol.wordBreak_v2("applepenapple", ["apple", "pen"]))
        self.assertFalse(self.sol.wordBreak_v2("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_wordBreak_v3(self):
        self.assertTrue(self.sol.wordBreak_v3("leetcode", ["leet", "code"]))
        self.assertTrue(self.sol.wordBreak_v3("applepenapple", ["apple", "pen"]))
        self.assertFalse(self.sol.wordBreak_v3("catsandog", ["cats", "dog", "sand", "and", "cat"]))
