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


class TestSolution(unittest.TestCase):
    def test_lastStoneWeight(self):
        solution = Solution()
        self.assertEqual(solution.last_stone_weight([2, 7, 4, 1, 8, 1]), 1)
        self.assertEqual(solution.last_stone_weight([2, 2]), 0)
        self.assertEqual(solution.last_stone_weight([2, 2, 2]), 2)
        self.assertEqual(solution.last_stone_weight([2, 2, 2, 2]), 0)
        self.assertEqual(solution.last_stone_weight([2, 2, 2, 2, 2]), 2)
        self.assertEqual(solution.last_stone_weight([2, 2, 2, 2, 2, 2]), 0)

    def test_lastStoneWeightV2(self):
        solution = Solution()
        self.assertEqual(solution.last_stone_weight_v2([2, 7, 4, 1, 8, 1]), 1)
        self.assertEqual(solution.last_stone_weight_v2([2, 2]), 0)
        self.assertEqual(solution.last_stone_weight_v2([2, 2, 2]), 2)
        self.assertEqual(solution.last_stone_weight_v2([2, 2, 2, 2]), 0)
        self.assertEqual(solution.last_stone_weight_v2([2, 2, 2, 2, 2]), 2)
        self.assertEqual(solution.last_stone_weight_v2([2, 2, 2, 2, 2, 2]), 0)
