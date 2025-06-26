from typing import List
import unittest


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            tmp = list(adj[src])
            for i, v in enumerate(tmp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
             ["JFK", "MUC", "LHR", "SFO", "SJC"]),
            ([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]],
             ["JFK", "NRT", "JFK", "KUL"]),
            ([["JFK", "ATL"], ["ATL", "JFK"]],
             ["JFK", "ATL", "JFK"]),
        ]

    def test_findItinerary(self):
        for tickets, expected in self.test_cases:
            with self.subTest(tickets=tickets, expected=expected):
                result = self.solution.findItinerary(tickets)
                self.assertEqual(result, expected)
