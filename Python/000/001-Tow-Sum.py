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


def two_sum_v2(nums: [int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1

    for i in range(len(nums)):
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1

    return []


def two_sum_v3(nums: [int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


#################### Test Case ####################
class TestTowSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_two_sum_v2(self):
        self.assertEqual(two_sum_v2([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum_v2([2, 3, 4], 6), [0, 2])
        self.assertEqual(two_sum_v2([3, 3], 6), [0, 1])

    def test_two_sum_v3(self):
        self.assertEqual(two_sum_v3([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum_v3([2, 3, 4], 6), [0, 2])
        self.assertEqual(two_sum_v3([3, 3], 6), [0, 1])
