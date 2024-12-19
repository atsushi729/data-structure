from typing import List
import unittest


#################### Solution ####################
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums) - self.k]


#################### Test Case ####################
class TestKthLargest(unittest.TestCase):
    def test_add(self):
        kth_largest = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(kth_largest.add(3), 4)
        self.assertEqual(kth_largest.add(5), 5)
        self.assertEqual(kth_largest.add(10), 5)
        self.assertEqual(kth_largest.add(9), 8)
        self.assertEqual(kth_largest.add(4), 8)
