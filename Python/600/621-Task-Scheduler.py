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


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_least_interval(self):
        self.assertEqual(Solution().least_interval(["A", "A", "A", "B", "B", "B"], 2), 8)

    def test_least_interval_v2(self):
        self.assertEqual(Solution().least_interval_v2(["A", "A", "A", "B", "B", "B"], 2), 8)