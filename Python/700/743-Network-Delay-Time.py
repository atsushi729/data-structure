from typing import List
import heapq
import collections
import unittest


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, start_node: int) -> int:
        graph = collections.defaultdict(list)

        for source, target, time_cost in times:
            graph[source].append((target, time_cost))

        # Priority queue: (elapsed_time, current_node)
        min_heap = [(0, start_node)]
        visited_nodes = set()
        max_delay = 0

        while min_heap:
            elapsed_time, current_node = heapq.heappop(min_heap)
            if current_node in visited_nodes:
                continue
            visited_nodes.add(current_node)
            max_delay = elapsed_time

            for neighbor, travel_time in graph[current_node]:
                if neighbor not in visited_nodes:
                    heapq.heappush(min_heap, (elapsed_time + travel_time, neighbor))

        return max_delay if len(visited_nodes) == n else -1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
            ([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1, 3),
            ([[1, 2, 5], [1, 3, 2], [2, 4, 1]], 4, 1, 6),
            ([[1, 2, 10], [2, 3, 5], [3, 4, 10]], 4, 1, 25),
        ]

    def test_networkDelayTime(self):
        for times, n, k, expected in self.test_cases:
            with self.subTest(times=times, n=n, k=k):
                result = self.solution.networkDelayTime(times, n, k)
                self.assertEqual(result, expected)
