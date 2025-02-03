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
    def test_can_finish(self):
        self.assertEqual(Solution().can_finish(3, [[1, 0], [2, 1]]), True)
        self.assertEqual(Solution().can_finish(2, [[1, 0]]), True)
        self.assertEqual(Solution().can_finish(2, [[1, 0], [0, 1]]), False)