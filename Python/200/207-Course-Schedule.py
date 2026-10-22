from typing import List
from collections import deque
import unittest


class Solution:
    def can_finish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Time complexity: O(n + e) where n is the number of courses and e is the number of prerequisites
        Space complexity: O(n + e) where n is the number of courses and e is the number of prerequisites
        """
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False

            if pre_map[crs] == []:
                return True

            visiting.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            pre_map[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

    def can_finish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return finish == numCourses


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_can_finish(self):
        test_cases = [
            # No prerequisites
            (2, [], True),
            (1, [], True),

            # Simple dependencies
            (2, [[1, 0]], True),
            (3, [[1, 0], [2, 1]], True),

            # Cyclic dependencies
            (2, [[1, 0], [0, 1]], False),
            (3, [[1, 0], [2, 1], [0, 2]], False),

            # Self dependency
            (1, [[0, 0]], False),

            # Multiple prerequisites
            (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),

            # Disconnected components
            (5, [[1, 0], [3, 2]], True),

            # Cycle in one component
            (5, [[1, 0], [0, 1], [3, 2]], False),

            # Additional edge cases
            (1, [], True),
            (4, [[1, 0], [2, 1], [3, 2]], True),
            (4, [[1, 0], [2, 1], [3, 2], [1, 3]], False),
        ]

        for method in [
            self.solution.can_finish,
            self.solution.can_finish2,
        ]:
            for num_courses, prerequisites, expected in test_cases:
                with self.subTest(
                        method=method.__name__,
                        num_courses=num_courses,
                        prerequisites=prerequisites,
                ):
                    self.assertEqual(
                        method(num_courses, prerequisites),
                        expected,
                    )


if __name__ == "__main__":
    unittest.main()
