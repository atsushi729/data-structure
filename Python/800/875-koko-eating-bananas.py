""""
Input data information
 - data type   : int
 - data range  : 1 <= pile.length <= 1,000
 - data format : array[i]

Note : 
 - If we get h with less than equal, then simply return 0.

Design:
## Brute force way
the range of k value:
1 <= k <= max(piles)
We can simply iterate and find minimum value of k which match condition.

## Better way
Binary search
We find min and max value of answer.
We can iterate through with binary search.
"""

import math
import unittest


#################### Solution ####################
class Solution:
    def min_eating_speed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            k = (left + right) // 2
            total_time = 0

            for p in piles:
                total_time += math.ceil(p / k)
            if total_time <= h:
                result = k
                right = k - 1
            else:
                left = k + 1
        return result


#################### Test Case ####################
class TestMinEatingSpeed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([3, 6, 7, 11], 8, 4),
            ([30, 11, 23, 4, 20], 5, 30),
            ([30, 11, 23, 4, 20], 6, 23),
            ([1, 4, 3, 2], 9, 2),
        ]

    def test_min_eating_speed(self):
        for piles, h, expected in self.test_cases:
            with self.subTest(piles=piles, h=h):
                result = self.s.min_eating_speed(piles, h)
                self.assertEqual(result, expected)
