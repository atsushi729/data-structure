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

    def minCostConnectPoints2(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        dist = [100000000] * n
        visit = [False] * n
        edges, res = 0, 0

        while edges < n - 1:
            visit[node] = True
            nextNode = -1
            for i in range(n):
                if visit[i]:
                    continue
                curDist = (abs(points[i][0] - points[node][0]) +
                           abs(points[i][1] - points[node][1]))
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i

            res += dist[nextNode]
            node = nextNode
            edges += 1

        return res

    def minCostConnectPoints3(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        dist = [100000000] * n
        visit = [False] * n
        edges, res = 0, 0

        while edges < n - 1:
            visit[node] = True
            nextNode = -1
            for i in range(n):
                if visit[i]:
                    continue
                curDist = (abs(points[i][0] - points[node][0]) +
                           abs(points[i][1] - points[node][1]))
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i

            res += dist[nextNode]
            node = nextNode
            edges += 1

        return res


class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True


class Solution2:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        edges = []

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        edges.sort()
        res = 0
        for dist, u, v in edges:
            if dsu.union(u, v):
                res += dist
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.solution2 = Solution2()
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

    def test_minCostConnectPoints2(self):
        for points, expected in self.test_cases:
            with self.subTest(points=points, expected=expected):
                result = self.solution.minCostConnectPoints2(points)
                self.assertEqual(result, expected)

    def test_minCostConnectPoints3(self):
        for points, expected in self.test_cases:
            with self.subTest(points=points, expected=expected):
                result = self.solution.minCostConnectPoints3(points)
                self.assertEqual(result, expected)

    def test_minCostConnectPoints_dsu(self):
        for points, expected in self.test_cases:
            with self.subTest(points=points, expected=expected):
                result = self.solution2.minCostConnectPoints(points)
                self.assertEqual(result, expected)
