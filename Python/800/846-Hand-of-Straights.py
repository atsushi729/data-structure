from collections import Counter
from typing import List
import heapq
import unittest


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}

        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

    def isNStraightHand2(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        hand.sort()

        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if count[i] <= 0:
                        return False
                    count[i] -= 1
        return True

    def isNStraightHand3(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)

        for num in hand:
            start = num

            while count[start - 1]:
                start -= 1
            while start <= num:
                while count[start]:
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1
                start += 1
        return True


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([1, 2, 3, 3, 4, 4, 5, 6], 4, True),
            ([1, 2, 3, 4], 3, False),
            ([1, 2, 3], 1, True),
            ([1, 2], 2, True),
            ([1], 1, True),
        ]

    def test_isNStraightHand(self):
        for hand, groupSize, expected in self.test_cases:
            with self.subTest(hand=hand, groupSize=groupSize):
                result = self.solution.isNStraightHand(hand, groupSize)
                self.assertEqual(result, expected)

    def test_isNStraightHand2(self):
        for hand, groupSize, expected in self.test_cases:
            with self.subTest(hand=hand, groupSize=groupSize):
                result = self.solution.isNStraightHand2(hand, groupSize)
                self.assertEqual(result, expected)

    def test_isNStraightHand3(self):
        for hand, groupSize, expected in self.test_cases:
            with self.subTest(hand=hand, groupSize=groupSize):
                result = self.solution.isNStraightHand3(hand, groupSize)
                self.assertEqual(result, expected)
