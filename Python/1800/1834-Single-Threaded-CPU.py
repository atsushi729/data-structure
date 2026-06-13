import heapq
import unittest
from copy import deepcopy


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

    def get_order_v2(self, tasks: list[list[int]]) -> list[int]:
        indexed_tasks = sorted(
            (enqueue_time, processing_time, index)
            for index, (enqueue_time, processing_time) in enumerate(tasks)
        )

        result = []
        available_tasks = []

        task_pointer = 0
        current_time = indexed_tasks[0][0]
        total_tasks = len(indexed_tasks)

        while available_tasks or task_pointer < total_tasks:
            while (
                    task_pointer < total_tasks
                    and indexed_tasks[task_pointer][0] <= current_time
            ):
                enqueue_time, processing_time, index = indexed_tasks[task_pointer]
                heapq.heappush(available_tasks, (processing_time, index))
                task_pointer += 1

            if available_tasks:
                processing_time, index = heapq.heappop(available_tasks)
                current_time += processing_time
                result.append(index)
            else:
                current_time = indexed_tasks[task_pointer][0]

        return result


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            (
                [[1, 2], [2, 4], [3, 2], [4, 1]],
                [0, 2, 3, 1],
            ),
            (
                [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]],
                [4, 3, 2, 0, 1],
            ),
        ]

    def test_get_order(self):
        for tasks, expected in self.test_cases:
            with self.subTest(tasks=tasks, expected=expected):
                self.assertEqual(
                    self.solution.get_order(deepcopy(tasks)),
                    expected,
                )

    def test_get_order_v2(self):
        for tasks, expected in self.test_cases:
            with self.subTest(tasks=tasks, expected=expected):
                self.assertEqual(
                    self.solution.get_order_v2(deepcopy(tasks)),
                    expected,
                )
