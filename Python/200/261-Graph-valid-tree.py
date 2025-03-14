from typing import List
import unittest
from collections import deque


#################### Solution ####################
class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False

        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for nei in graph[node]:
                if nei != parent and not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n

    def valid_tree_v2(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        q = deque([(0, -1)])
        visited.add(0)

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                visited.add(nei)
                q.append((nei, node))

        return len(visited) == n


###################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_validTree(self):
        solution = Solution()
        self.assertEqual(solution.valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True)
        self.assertEqual(solution.valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False)
        self.assertEqual(solution.valid_tree(5, [[0, 1], [1, 2], [3, 4]]), False)
        self.assertEqual(solution.valid_tree(1, []), True)
        self.assertEqual(solution.valid_tree(2, [[0, 1]]), True)
        self.assertEqual(solution.valid_tree(2, []), False)
        self.assertEqual(solution.valid_tree(3, [[0, 1], [1, 2]]), True)
        self.assertEqual(solution.valid_tree(3, [[0, 1], [1, 2], [2, 0]]), False)
        self.assertEqual(solution.valid_tree(4, [[0, 1], [1, 2], [2, 3]]), True)
        self.assertEqual(solution.valid_tree(4, [[0, 1], [1, 2], [2, 3], [3, 0]]), False)

    def test_valid_tree_v2(self):
        solution = Solution()
        self.assertEqual(solution.valid_tree_v2(5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True)
        self.assertEqual(solution.valid_tree_v2(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False)
        self.assertEqual(solution.valid_tree_v2(5, [[0, 1], [1, 2], [3, 4]]), False)
        self.assertEqual(solution.valid_tree_v2(1, []), True)
        self.assertEqual(solution.valid_tree_v2(2, [[0, 1]]), True)
        self.assertEqual(solution.valid_tree_v2(2, []), False)
        self.assertEqual(solution.valid_tree_v2(3, [[0, 1], [1, 2]]), True)
        self.assertEqual(solution.valid_tree_v2(3, [[0, 1], [1, 2], [2, 0]]), False)
        self.assertEqual(solution.valid_tree_v2(4, [[0, 1], [1, 2], [2, 3]]), True)
        self.assertEqual(solution.valid_tree_v2(4, [[0, 1], [1, 2], [2, 3], [3, 0]]), False)
