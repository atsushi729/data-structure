from typing import List
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
        ]

        for num_courses, prerequisites, expected in test_cases:
            with self.subTest(
                    num_courses=num_courses,
                    prerequisites=prerequisites,
            ):
                self.assertEqual(
                    self.solution.can_finish(num_courses, prerequisites),
                    expected,
                )


if __name__ == "__main__":
    unittest.main()
