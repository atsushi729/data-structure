import unittest


#################### Solution ####################
def find_duplicate(nums: list[int]) -> int:
    """
    Hash Set
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = set()

    for num in nums:
        if num in seen:
            return num
        else:
            seen.add(num)
    return -1


def find_duplicate_v2(nums: list[int]) -> int:
    """
    Floyd's Tortoise and Hare (Cycle Detection)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


#################### Test Case ####################
class TestFindDuplicate(unittest.TestCase):
    def test_find_duplicate(self):
        self.assertEqual(find_duplicate([1, 3, 4, 2, 2]), 2)
        self.assertEqual(find_duplicate([3, 1, 3, 4, 2]), 3)
        self.assertEqual(find_duplicate([1, 1]), 1)
        self.assertEqual(find_duplicate([1, 1, 2]), 1)
        self.assertEqual(find_duplicate([2, 2, 2, 2, 2]), 2)

    def test_find_duplicate_v2(self):
        self.assertEqual(find_duplicate_v2([1, 3, 4, 2, 2]), 2)
        self.assertEqual(find_duplicate_v2([3, 1, 3, 4, 2]), 3)
        self.assertEqual(find_duplicate_v2([1, 1]), 1)
        self.assertEqual(find_duplicate_v2([1, 1, 2]), 1)
        self.assertEqual(find_duplicate_v2([2, 2, 2, 2, 2]), 2)
