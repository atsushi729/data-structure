from typing import List
import heapq
import collections
import unittest


class Solution:
    def network_delay_time(self, times: List[List[int]], n: int, start_node: int) -> int:
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

    def network_delay_time2(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        dist = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node, time):
            if time >= dist[node]:
                return

            dist[node] = time
            for nei, w in adj[node]:
                dfs(nei, time + w)

        dfs(k, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1

    def network_delay_time3(self, times: List[List[int]], n: int, k: int) -> int:
        inf = float('inf')
        dist = [[inf] * n for _ in range(n)]

        for u, v, w in times:
            dist[u - 1][v - 1] = w
        for i in range(n):
            dist[i][i] = 0

        for mid in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][mid] + dist[mid][j])

        res = max(dist[k - 1])
        return res if res < inf else -1

    def network_delay_time4(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        min_heap = [(0, k)]
        visit = set()
        total = 0

        while min_heap:
            weight1, node1 = heapq.heappop(min_heap)

            if node1 in visit:
                continue

            visit.add(node1)
            total = weight1

            for node2, weight2 in edges[node1]:
                if node2 not in visit:
                    heapq.heappush(min_heap, (weight1 + weight2, node2))

        return total if len(visit) == n else -1

    def network_delay_time5(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[k - 1] = 0
        for _ in range(n - 1):
            for u, v, w in times:
                if dist[u - 1] + w < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + w
        max_dist = max(dist)
        return max_dist if max_dist < float('inf') else -1

    def network_delay_time6(self, times: List[List[int]], n: int, k: int) -> int:
        # Build the graph: adjacency list mapping each node to its neighbors and weights
        graph = collections.defaultdict(list)
        for start, end, time in times:
            graph[start].append((end, time))

        # Priority queue: (current total time, node)
        min_heap = [(0, k)]  # Start from node k with time 0
        visited = set()  # Track visited nodes
        max_time = 0  # Maximum time needed to reach all nodes

        while min_heap:
            current_time, current_node = heapq.heappop(min_heap)

            # Skip if node has already been visited
            if current_node in visited:
                continue

            # Mark node as visited and update maximum time
            visited.add(current_node)
            max_time = current_time

            # Explore neighboring nodes
            for next_node, travel_time in graph[current_node]:
                if next_node not in visited:
                    heapq.heappush(min_heap, (current_time + travel_time, next_node))

        # Return max_time if all nodes are visited, otherwise -1
        return max_time if len(visited) == n else -1


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

    def test_network_delay_time(self):
        for times, n, k, expected in self.test_cases:
            with self.subTest(times=times, n=n, k=k):
                result = self.solution.network_delay_time(times, n, k)
                self.assertEqual(result, expected)

    def test_network_delay_time2(self):
        for times, n, k, expected in self.test_cases:
            with self.subTest(times=times, n=n, k=k):
                result = self.solution.network_delay_time2(times, n, k)
                self.assertEqual(result, expected)

    def test_network_delay_time3(self):
        for times, n, k, expected in self.test_cases:
            with self.subTest(times=times, n=n, k=k):
                result = self.solution.network_delay_time3(times, n, k)
                self.assertEqual(result, expected)

    def test_network_delay_time4(self):
        for times, n, k, expected in self.test_cases:
            with self.subTest(times=times, n=n, k=k):
                result = self.solution.network_delay_time4(times, n, k)
                self.assertEqual(result, expected)

    def test_network_delay_time5(self):
        for times, n, k, expected in self.test_cases:
            with self.subTest(times=times, n=n, k=k):
                result = self.solution.network_delay_time5(times, n, k)
                self.assertEqual(result, expected)

    def test_network_delay_time6(self):
        for times, n, k, expected in self.test_cases:
            with self.subTest(times=times, n=n, k=k):
                result = self.solution.network_delay_time6(times, n, k)
                self.assertEqual(result, expected)
