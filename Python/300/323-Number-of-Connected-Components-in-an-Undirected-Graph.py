from typing import List
import unittest
from collections import deque


class Solution:
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res

    def count_components_v2(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([node])
            visit[node] = True
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                res += 1
        return res


class TestSolution(unittest.TestCase):
    def test_countComponents(self):
        solution = Solution()
        self.assertEqual(solution.count_components(5, [[0, 1], [1, 2], [3, 4]]), 2)
        self.assertEqual(solution.count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1)
        self.assertEqual(solution.count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]), 1)
        self.assertEqual(solution.count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4], [2, 4]]), 1)
        self.assertEqual(solution.count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4], [2, 4], [0, 2]]), 1)

    def test_count_components_v2(self):
        solution = Solution()
        self.assertEqual(solution.count_components_v2(5, [[0, 1], [1, 2], [3, 4]]), 2)
        self.assertEqual(solution.count_components_v2(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1)
        self.assertEqual(solution.count_components_v2(5, [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]), 1)
        self.assertEqual(solution.count_components_v2(5, [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4], [2, 4]]), 1)
        self.assertEqual(solution.count_components_v2(5, [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4], [2, 4], [0, 2]]), 1)