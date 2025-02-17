from typing import List
import unittest


#################### Solution ####################
class Solution:
    def min_cost_climbing_stairs(self, cost: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_min_cost_climbing_stairs(self):
        solution = Solution()
        self.assertEqual(solution.min_cost_climbing_stairs([10, 15, 20]), 15)
        self.assertEqual(solution.min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)
