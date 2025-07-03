from typing import List
from collections import defaultdict
import unittest
import heapq


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

    def findItinerary3(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []

        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]

    def findItinerary4(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)

        res = []

        def dfs(cur):
            while adj[cur]:
                next = heapq.heappop(adj[cur])
                dfs(next)
            res.append(cur)

        dfs("JFK")
        return res[::-1]

    def findItinerary5(self, tickets: List[List[str]]) -> List[str]:
        # Initialize an adjacency list to represent the graph
        adj_list = defaultdict(list)

        # Sort tickets in reverse lexical order and build the adjacency list
        for src, dst in sorted(tickets, reverse=True):
            adj_list[src].append(dst)

        # Stack to perform DFS; we always start from 'JFK'
        stack = ["JFK"]
        itinerary = []

        # Perform DFS traversal
        while stack:
            current = stack[-1]

            # If there are no more destinations to visit from current airport, add it to the result (we're backtracking)
            if not adj_list[current]:
                itinerary.append(stack.pop())
            else:
                # Otherwise, keep visiting the next lexical smallest destination
                stack.append(adj_list[current].pop())

        # The itinerary is built in reverse, so we reverse it at the end
        return itinerary[::-1]


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

    def test_findItinerary3(self):
        for tickets, expected in self.test_cases:
            with self.subTest(tickets=tickets, expected=expected):
                result = self.solution.findItinerary3(tickets)
                self.assertEqual(result, expected)

    def test_findItinerary4(self):
        for tickets, expected in self.test_cases:
            with self.subTest(tickets=tickets, expected=expected):
                result = self.solution.findItinerary4(tickets)
                self.assertEqual(result, expected)

    def test_findItinerary5(self):
        for tickets, expected in self.test_cases:
            with self.subTest(tickets=tickets, expected=expected):
                result = self.solution.findItinerary5(tickets)
                self.assertEqual(result, expected)
