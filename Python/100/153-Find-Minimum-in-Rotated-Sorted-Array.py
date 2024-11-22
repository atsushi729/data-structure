import unittest


#################### Solution ####################
def find_min(nums: list[int]) -> int:
    start, end = 0, len(nums) - 1
    curr_min = float("inf")

    while start < end:
        mid = (start + end) // 2
        curr_min = min(curr_min, nums[mid])

        # right has the min
        if nums[mid] > nums[end]:
            start = mid + 1

        # left has the  min
        else:
            end = mid - 1

    return min(curr_min, nums[start])


#################### Test Case ####################
class TestFindMin(unittest.TestCase):
    def test_findMin(self):
        self.assertEqual(find_min([3, 4, 5, 1, 2]), 1)
        self.assertEqual(find_min([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(find_min([11, 13, 15, 17]), 11)
        self.assertEqual(find_min([2, 1]), 1)
        self.assertEqual(find_min([1]), 1)
