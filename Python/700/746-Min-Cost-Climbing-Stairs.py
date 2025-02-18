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

    def min_cost_climbing_stairs_v2(self, cost: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        cache = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0

            if cache[i] != -1:
                return cache[i]

            cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return cache[i]

        return min(dfs(0), dfs(1))


    def min_cost_climbing_stairs_v3(self, cost: List[int]) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        def dfs(i):
            if i >= len(cost):
                return 0
            return cost[i] + min(dfs(i + 1), dfs(i + 2))

        return min(dfs(0), dfs(1))

#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_min_cost_climbing_stairs(self):
        solution = Solution()
        self.assertEqual(solution.min_cost_climbing_stairs([10, 15, 20]), 15)
        self.assertEqual(solution.min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)

    def test_min_cost_climbing_stairs_v2(self):
        solution = Solution()
        self.assertEqual(solution.min_cost_climbing_stairs_v2([10, 15, 20]), 15)
        self.assertEqual(solution.min_cost_climbing_stairs_v2([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)

    def test_min_cost_climbing_stairs_v3(self):
        solution = Solution()
        self.assertEqual(solution.min_cost_climbing_stairs_v3([10, 15, 20]), 15)
        self.assertEqual(solution.min_cost_climbing_stairs_v3([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)