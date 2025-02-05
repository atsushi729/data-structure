from typing import List
import unittest


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_findOrder(self):
        self.assertEqual(Solution().findOrder(2, [[1, 0]]), [0, 1])
        self.assertEqual(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]), [0, 1, 2, 3])
        self.assertEqual(Solution().findOrder(1, []), [0])
