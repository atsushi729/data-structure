from typing import List
import unittest


class Solution:
    def can_complete_circuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        start = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1

        return start


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
            ([2, 3, 4], [3, 4, 3], -1),
            ([5], [4], 0),
            ([1, 2], [2, 1], 1),
            ([2, 3], [3, 2], 1),
        ]

    def test_can_complete_circuit(self):
        for gas, cost, expected in self.test_cases:
            with self.subTest(gas=gas, cost=cost):
                result = self.solution.can_complete_circuit(gas, cost)
                self.assertEqual(result, expected)
