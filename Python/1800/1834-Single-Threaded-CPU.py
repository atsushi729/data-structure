import heapq
import unittest


class Solution:
    def get_order(self, tasks: list[list[int]]) -> list[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t: t[0])

        res, min_heap = [], []
        i, time = 0, tasks[0][0]

        while min_heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1
            if not min_heap:
                time = tasks[i][0]
            else:
                process_time, index = heapq.heappop(min_heap)
                time += process_time
                res.append(index)
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([[1, 2], [2, 4], [3, 2], [4, 1]], [0, 2, 3, 1]),
            ([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]], [4, 3, 2, 0, 1]),
        ]

    def test_get_order(self):
        for tasks, expected in self.test_cases:
            with self.subTest(tasks=tasks, expected=expected):
                self.assertEqual(
                    self.solution.get_order(tasks[:]),
                    expected
                )
