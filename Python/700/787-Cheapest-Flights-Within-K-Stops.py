from typing import List
import unittest


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
