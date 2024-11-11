import unittest


def find_duplicate(nums: list[int]) -> int:
    seen = set()

    for num in nums:
        if num in seen:
            return num
        else:
            seen.add(num)
    return -1


class TestFindDuplicate(unittest.TestCase):
    def test_find_duplicate(self):
        self.assertEqual(find_duplicate([1, 3, 4, 2, 2]), 2)
        self.assertEqual(find_duplicate([3, 1, 3, 4, 2]), 3)
        self.assertEqual(find_duplicate([1, 1]), 1)
        self.assertEqual(find_duplicate([1, 1, 2]), 1)
        self.assertEqual(find_duplicate([2, 2, 2, 2, 2]), 2)
