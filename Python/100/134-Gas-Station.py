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

    def can_complete_circuit2(self, gas: List[int], cost: List[int]) -> int:
        total_station = len(gas)

        for start in range(total_station):
            fuel_in_tank = gas[start] - cost[start]

            if fuel_in_tank < 0:
                continue

            current_station = (start + 1) % total_station

            while current_station != start:
                fuel_in_tank += gas[current_station] - cost[current_station]

                if fuel_in_tank < 0:
                    break

                current_station = (current_station + 1) % total_station

            if current_station == start:
                return start

        return -1

    def can_complete_circuit3(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start, end = n - 1, 0
        tank = gas[start] - cost[start]
        while start > end:
            if tank < 0:
                start -= 1
                tank += gas[start] - cost[start]
            else:
                tank += gas[end] - cost[end]
                end += 1
        return start if tank >= 0 else -1


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

    def test_can_complete_circuit2(self):
        for gas, cost, expected in self.test_cases:
            with self.subTest(gas=gas, cost=cost):
                result = self.solution.can_complete_circuit2(gas, cost)
                self.assertEqual(result, expected)

    def test_can_complete_circuit3(self):
        for gas, cost, expected in self.test_cases:
            with self.subTest(gas=gas, cost=cost):
                result = self.solution.can_complete_circuit3(gas, cost)
                self.assertEqual(result, expected)
