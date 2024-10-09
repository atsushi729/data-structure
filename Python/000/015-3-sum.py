import unittest


#################### Solution ####################
def threeSum(nums: list[int]) -> list[list[int]]:
    res = set()
    nums.sort()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    tmp = [nums[i], nums[j], nums[k]]
                    res.add(tuple(tmp))
    return [list(i) for i in res]


#################### Test Case ####################
class TestThreeSum(unittest.TestCase):
    def test_three_sum(self):
        self.assertEqual(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(threeSum([]), [])
        self.assertEqual(threeSum([0]), [])
        self.assertEqual(threeSum([0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(threeSum([0, 0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(threeSum([0, 0, 0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(threeSum([-1, 0, 1, 0]), [[-1, 0, 1]])
        self.assertEqual(threeSum([1, 1, -2]), [[-2, 1, 1]])
        self.assertEqual(threeSum([3, 0, -2, -1, 1, 2]), [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]])
