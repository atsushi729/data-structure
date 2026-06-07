from typing import List
import unittest
import heapq


class Solution:
    def last_stone_weight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)

        return stones[0] if stones else 0

    def last_stone_weight_v2(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, x - y)

        return -stones[0] if stones else 0

    def last_stone_weight_v3(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second != first:
                heapq.heappush(stones, first - second)

        return abs(stones[0]) if stones else 0


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([2, 7, 4, 1, 8, 1], 1),
            ([2, 2], 0),
            ([2, 2, 2], 2),
            ([2, 2, 2, 2], 0),
            ([2, 2, 2, 2, 2], 2),
            ([2, 2, 2, 2, 2, 2], 0),
        ]

    def test_last_stone_weight(self):
        for stones, expected in self.test_cases:
            with self.subTest(stones=stones, expected=expected):
                self.assertEqual(
                    self.solution.last_stone_weight(stones[:]),
                    expected
                )

    def test_last_stone_weight_v2(self):
        for stones, expected in self.test_cases:
            with self.subTest(stones=stones, expected=expected):
                self.assertEqual(
                    self.solution.last_stone_weight_v2(stones[:]),
                    expected
                )

    def test_last_stone_weight_v3(self):
        for stones, expected in self.test_cases:
            with self.subTest(stones=stones, expected=expected):
                self.assertEqual(
                    self.solution.last_stone_weight_v3(stones[:]),
                    expected
                )


if __name__ == "__main__":
    unittest.main()
