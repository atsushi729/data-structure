from typing import List
import heapq
import unittest


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0
        visit = set()
        minH = [[0, 0]]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
            ([[3, 12], [-2, 5], [-4, 1]], 18),
            ([[0, 0], [1, 1], [1, 0], [0, 1]], 3),
            ([[0, 0]], 0),
        ]

    def test_minCostConnectPoints(self):
        for points, expected in self.test_cases:
            with self.subTest(points=points, expected=expected):
                result = self.solution.minCostConnectPoints(points)
                self.assertEqual(result, expected)