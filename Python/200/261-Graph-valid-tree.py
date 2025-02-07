from typing import List
import unittest


#################### Solution ####################
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
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


###################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_validTree(self):
        solution = Solution()
        self.assertEqual(solution.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True)
        self.assertEqual(solution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False)
        self.assertEqual(solution.validTree(5, [[0, 1], [1, 2], [3, 4]]), False)
        self.assertEqual(solution.validTree(1, []), True)
        self.assertEqual(solution.validTree(2, [[0, 1]]), True)
        self.assertEqual(solution.validTree(2, []), False)
        self.assertEqual(solution.validTree(3, [[0, 1], [1, 2]]), True)
        self.assertEqual(solution.validTree(3, [[0, 1], [1, 2], [2, 0]]), False)
        self.assertEqual(solution.validTree(4, [[0, 1], [1, 2], [2, 3]]), True)
        self.assertEqual(solution.validTree(4, [[0, 1], [1, 2], [2, 3], [3, 0]]), False)
