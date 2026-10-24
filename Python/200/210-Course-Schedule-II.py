from typing import List
from collections import deque
import unittest


#################### Solution ####################
class Solution:
    def find_order(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        cycle, visiting = set(), set()
        output = []

        def check(crs):
            if crs in cycle:
                return False

            if crs in visiting:
                return True

            cycle.add(crs)
            for pre in pre_map[crs]:
                if not check(pre):
                    return False

            cycle.remove(crs)
            visiting.add(crs)
            output.append(crs)
            return True

        for i in range(numCourses):
            if not check(i):
                return []

        return output

    def find_order2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1

        queue = deque(
            i for i in range(numCourses) if in_degree[i] == 0
        )
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in graph[course]:
                in_degree[next_course] -= 1

                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return order if len(order) == numCourses else []


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_order(self):
        test_cases = [
            # No prerequisites
            (1, [], True),
            (2, [], True),

            # Simple dependencies
            (2, [[1, 0]], True),
            (3, [[1, 0], [2, 1]], True),

            # Multiple prerequisites
            (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),

            # Disconnected components
            (5, [[1, 0], [3, 2]], True),

            # Cyclic dependencies
            (2, [[1, 0], [0, 1]], False),
            (3, [[1, 0], [2, 1], [0, 2]], False),

            # Self dependency
            (1, [[0, 0]], False),

            # Cycle in one component
            (5, [[1, 0], [0, 1], [3, 2]], False),
        ]

        methods = [
            self.solution.find_order,
            self.solution.find_order2,
        ]

        for method in methods:
            for num_courses, prerequisites, expected in test_cases:
                with self.subTest(
                        method=method.__name__,
                        num_courses=num_courses,
                        prerequisites=prerequisites,
                ):
                    result = method(num_courses, prerequisites)

                    if not expected:
                        self.assertEqual(result, [])
                        continue

                    # All courses must appear exactly once
                    self.assertEqual(len(result), num_courses)
                    self.assertEqual(
                        set(result),
                        set(range(num_courses)),
                    )

                    # Prerequisites must come before their courses
                    position = {
                        course: i
                        for i, course in enumerate(result)
                    }

                    for course, prerequisite in prerequisites:
                        self.assertLess(
                            position[prerequisite],
                            position[course],
                        )


if __name__ == "__main__":
    unittest.main()
