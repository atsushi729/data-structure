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
def min_eating_speed(piles: list[int], h: int) -> int:
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
    def test_min_eating_speed(self):
        self.assertEqual(min_eating_speed([1, 4, 3, 2], 9), 2)
