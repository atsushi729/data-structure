from typing import List
import unittest


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3

    def mergeTriplets2(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = [False] * 3

        for t in triplets:
            if any(t[i] > target[i] for i in range(3)):
                continue
            for i in range(3):
                if t[i] == target[i]:
                    good[i] = True
        return all(good)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([[1, 2, 3], [7, 1, 1]], [7, 2, 3], True),
            ([[2, 5, 6], [1, 4, 4], [5, 7, 5]], [5, 4, 6], False),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 1, 1], True),
            ([[2, 3, 4], [5, 6, 7]], [2, 3, 4], True),
        ]

    def test_mergeTriplets(self):
        for triplets, target, expected in self.test_cases:
            with self.subTest(triplets=triplets, target=target, expected=expected):
                result = self.solution.mergeTriplets(triplets, target)
                self.assertEqual(result, expected)

    def test_mergeTriplets2(self):
        for triplets, target, expected in self.test_cases:
            with self.subTest(triplets=triplets, target=target, expected=expected):
                result = self.solution.mergeTriplets2(triplets, target)
                self.assertEqual(result, expected)
