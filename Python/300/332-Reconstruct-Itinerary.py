from typing import List
from collections import defaultdict
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

    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        stack = ["JFK"]
        res = []

        while stack:
            cur = stack[-1]
            if not adj[cur]:
                res.append(stack.pop())
            else:
                stack.append(adj[cur].pop())
        return res[::-1]


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

    def test_findItinerary2(self):
        for tickets, expected in self.test_cases:
            with self.subTest(tickets=tickets, expected=expected):
                result = self.solution.findItinerary2(tickets)
                self.assertEqual(result, expected)
