from typing import List
import unittest


class Solution:
    def find_redundant_connection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(node, par):
            if visit[node]:
                return True

            visit[node] = True

            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = [False] * (n + 1)

            if dfs(u, -1):
                return [u, v]

        return []


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_findRedundantConnection(self):
        solution = Solution()
        self.assertListEqual(solution.find_redundant_connection([[1, 2], [1, 3], [2, 3]]), [2, 3])
        self.assertListEqual(solution.find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]), [1, 4])
        self.assertListEqual(solution.find_redundant_connection([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]), [1, 3])
        self.assertListEqual(solution.find_redundant_connection([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5], [3, 5]]), [1, 3])
