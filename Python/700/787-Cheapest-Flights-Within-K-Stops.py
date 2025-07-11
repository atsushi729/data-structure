from typing import List
import unittest
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmp_prices = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmp_prices[d]:
                    tmp_prices[d] = prices[s] + p
            prices = tmp_prices
        return -1 if prices[dst] == float("inf") else prices[dst]

    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        adj = [[] for _ in range(n)]
        dist = [[INF] * (k + 5) for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])

        dist[src][0] = 0
        minHeap = [(0, src, -1)]  # cost, node, stops
        while len(minHeap):
            cst, node, stops = heapq.heappop(minHeap)
            if dst == node: return cst
            if stops == k or dist[node][stops + 1] < cst:
                continue
            for nei, w in adj[node]:
                nextCst = cst + w
                nextStops = 1 + stops
                if dist[nei][nextStops + 1] > nextCst:
                    dist[nei][nextStops + 1] = nextCst
                    heapq.heappush(minHeap, (nextCst, nei, nextStops))

        return -1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
            (4, [[0, 1, 200], [1, 2, 100], [1, 3, 300], [2, 3, 100]], 0, 3, 1, 500),
            (4, [[0, 1, 50], [1, 2, 50], [2, 3, 50], [0, 3, 200]], 0, 3, 2, 150),
        ]

    def test_findCheapestPrice(self):
        for n, flights, src, dst, k, expected in self.test_cases:
            with self.subTest(n=n, flights=flights, src=src, dst=dst, k=k):
                result = self.solution.findCheapestPrice(n, flights, src, dst, k)
                self.assertEqual(result, expected)

    def test_findCheapestPrice2(self):
        for n, flights, src, dst, k, expected in self.test_cases:
            with self.subTest(n=n, flights=flights, src=src, dst=dst, k=k):
                result = self.solution.findCheapestPrice2(n, flights, src, dst, k)
                self.assertEqual(result, expected)
