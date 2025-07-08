from collections import deque
import unittest


class Solution:
    def foreign_dictionary(self, words):
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while q:
            char = q.popleft()
            res.append(char)
            for neighbor in adj[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(res) != len(indegree):
            return ""

        return "".join(res)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_case = [
            (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
            (["z", "x"], "zx"),
            (["z", "x", "z"], ""),
            (["abc", "ab"], ""),
            (["a", "b", "c"], "abc"),
        ]

    def test_foreign_dictionary(self):
        for words, expected in self.test_case:
            with self.subTest(words=words, expected=expected):
                result = self.solution.foreign_dictionary(words)
                self.assertEqual(result, expected)
