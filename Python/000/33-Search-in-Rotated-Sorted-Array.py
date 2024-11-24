import unittest


def search(nums: list[int], target: int) -> int:
    """
    Time complexity: O(log n)
    Space complexity: O(1)
    """
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m

        if nums[l] <= nums[m]:
            if target < nums[l] or target > nums[m]:
                l = m + 1
            else:
                r = m - 1

        else:
            if target > nums[r] or target < nums[m]:
                r = m - 1
            else:
                l = m + 1
    return -1


class TestSearch(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(search([1], 0), -1)
        self.assertEqual(search([1], 1), 0)
