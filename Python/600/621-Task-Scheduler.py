import heapq
from collections import Counter, deque
from typing import List
import unittest


#################### Solution ####################
class Solution:
    def least_interval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)

        task_heap = [-count for count in task_counts.values()]
        heapq.heapify(task_heap)

        current_time = 0
        cooldown_queue = deque()

        while task_heap or cooldown_queue:
            current_time += 1

            if task_heap:
                remaining_count = 1 + heapq.heappop(task_heap)
                if remaining_count < 0:
                    cooldown_queue.append([remaining_count, current_time + n])
            else:
                if cooldown_queue:
                    next_available_time = cooldown_queue[0][1]
                    current_time = next_available_time
            if cooldown_queue and cooldown_queue[0][1] == current_time:
                heapq.heappush(task_heap, cooldown_queue.popleft()[0])

        return current_time

    def least_interval_v2(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_count = max(task_counts.values())
        max_count_tasks = sum(1 for count in task_counts.values() if count == max_count)

        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)

    def least_interval_v3(self, tasks: List[str], n: int) -> int:
        count = [0] * 26

        for task in tasks:
            count[ord(task) - ord("A")] += 1

        count.sort()
        maxf = count[25]
        idle = (maxf - 1) * n

        for i in range(24, -1, -1):
            idle -= min(maxf - 1, count[i])
        return max(0, idle) + len(tasks)

    def least_interval_v4(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)

        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        current_time = 0
        cooldown_queue = deque()  # (remaining_count, available_time)

        while max_heap or cooldown_queue:
            current_time += 1

            if max_heap:
                remaining_count = heapq.heappop(max_heap) + 1

                if remaining_count < 0:
                    cooldown_queue.append((remaining_count, current_time + n))

            elif cooldown_queue:
                current_time = cooldown_queue[0][1]

            while cooldown_queue and cooldown_queue[0][1] <= current_time:
                remaining_count, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, remaining_count)

        return current_time


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            # name, tasks, n, expected

            # Basic example from the problem statement
            (
                "Base case",
                ["A", "A", "A", "B", "B", "B"],
                2,
                8,
            ),

            # No cooldown period
            (
                "No cooldown",
                ["A", "A", "A", "B", "B", "B"],
                0,
                6,
            ),

            # Idle slots are required
            (
                "Idle required",
                ["A", "A", "A", "B", "B", "B"],
                3,
                10,
            ),

            # Only one task
            (
                "Single task",
                ["A"],
                2,
                1,
            ),

            # All tasks are unique
            (
                "All unique tasks",
                ["A", "B", "C", "D"],
                3,
                4,
            ),

            # Only one type of task
            (
                "Single task type",
                ["A", "A", "A", "A"],
                2,
                10,
            ),

            # Multiple tasks share the maximum frequency
            (
                "Two max frequency tasks",
                ["A", "A", "A", "B", "B", "B", "C", "C"],
                2,
                8,
            ),

            # Three tasks share the maximum frequency
            (
                "Three max frequency tasks",
                ["A", "A", "A", "B", "B", "B", "C", "C", "C"],
                2,
                9,
            ),

            # Enough tasks exist to fill all idle slots
            (
                "No idle slots needed",
                ["A", "A", "A", "B", "B", "B", "C", "C", "D", "D"],
                2,
                10,
            ),

            # Large cooldown period
            (
                "Large cooldown",
                ["A", "A", "B"],
                50,
                52,
            ),

            # Official LeetCode example
            (
                "LeetCode example",
                [
                    "A", "A", "A", "A", "A", "A",
                    "B", "C", "D", "E", "F", "G"
                ],
                2,
                16,
            ),
        ]

    def test_least_interval(self):
        for name, tasks, n, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.least_interval(tasks, n),
                    expected,
                )

    def test_least_interval_v2(self):
        for name, tasks, n, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.least_interval_v2(tasks, n),
                    expected,
                )

    def test_least_interval_v3(self):
        for name, tasks, n, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.least_interval_v3(tasks, n),
                    expected,
                )

    def test_least_interval_v4(self):
        for name, tasks, n, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.least_interval_v4(tasks, n),
                    expected,
                )
