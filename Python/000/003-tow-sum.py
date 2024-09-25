import unittest


#################### Solution ####################
def two_sum(nums: [int], target: int) -> list[int]:
    prevMap = {}  # val -> index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

    return []


#################### Test Case ####################
class TestTowSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_two_sum_v1(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_two_sum_v2(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_two_sum(self):
        self.assertEqual(two_sum([1, 2, 5, 6, 3], 9), [3, 4])
