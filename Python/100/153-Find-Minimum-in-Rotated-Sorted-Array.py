import unittest


#################### Solution ####################
def find_min(nums: list[int]) -> int:
    """
    Time complexity: O(log n)
    Space complexity: O(1)
    """
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


def find_min_v2(nums: list[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    return min(nums)


def find_min_v3(nums: list[int]) -> int:
    """
    Time complexity: O(log n)
    Space complexity: O(1)
    """
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        m = (l + r) // 2
        res = min(res, nums[m])

        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1

    return res


#################### Test Case ####################
class TestFindMin(unittest.TestCase):
    def test_findMin(self):
        self.assertEqual(find_min([3, 4, 5, 1, 2]), 1)
        self.assertEqual(find_min([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(find_min([11, 13, 15, 17]), 11)
        self.assertEqual(find_min([2, 1]), 1)
        self.assertEqual(find_min([1]), 1)

    def test_findMin_v2(self):
        self.assertEqual(find_min_v2([3, 4, 5, 1, 2]), 1)
        self.assertEqual(find_min_v2([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(find_min_v2([11, 13, 15, 17]), 11)
        self.assertEqual(find_min_v2([2, 1]), 1)
        self.assertEqual(find_min_v2([1]), 1)

    def test_findMin_v3(self):
        self.assertEqual(find_min_v3([3, 4, 5, 1, 2]), 1)
        self.assertEqual(find_min_v3([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(find_min_v3([11, 13, 15, 17]), 11)
        self.assertEqual(find_min_v3([2, 1]), 1)
        self.assertEqual(find_min_v3([1]), 1)
