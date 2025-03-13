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


class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_wordBreak(self):
        self.assertTrue(self.sol.wordBreak("leetcode", ["leet", "code"]))
        self.assertTrue(self.sol.wordBreak("applepenapple", ["apple", "pen"]))
        self.assertFalse(self.sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
