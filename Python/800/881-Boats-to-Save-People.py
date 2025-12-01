import unittest
from typing import List


class Solution:
    def num_rescue_boats(self, people: List[int], limit: int) -> int:
        """
        Time complexity: O(n log n)
        Space complexity: O(1)
        """
        people.sort()
        res, l, r = 0, 0, len(people) - 1

        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res

    def num_rescue_boats_v2(self, people: List[int], limit: int) -> int:
        """
        Time complexity: O(n + m) where m is the max weight in people
        Space complexity: O(m)
        """
        m = max(people)
        count = [0] * (m + 1)
        for p in people:
            count[p] += 1

        idx, i = 0, 1

        while idx < len(people):
            while count[i] == 0:
                i += 1
            people[idx] = i
            count[i] -= 1
            idx += 1

        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([1, 2], 3, 1),
            ([3, 2, 2, 1], 3, 3),
            ([3, 5, 3, 4], 5, 4),
            ([1, 1, 1, 1, 1, 1], 3, 3),
        ]

    def test_num_rescue_boats(self):
        for people, limit, expected in self.test_cases:
            self.assertEqual(self.s.num_rescue_boats(people, limit), expected)

    def test_num_rescue_boats_v2(self):
        for people, limit, expected in self.test_cases:
            self.assertEqual(self.s.num_rescue_boats_v2(people, limit), expected)
