"""
Title: Move Zeroes
    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Input data:
    type: list[int]
    data range: 1 <= len(nums) <= 10^4

Example:    1  3  12 i-> replace with 0   j
    nums = [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

Note:
    we can create extra array to store non-zero elements and zero elements.

Design:
"""

import unittest


def move_zeroes(nums: list[int]) -> list[int]:
    left, right = 0, 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    return nums


#################### Test Case ####################
class TestMoveZeroes(unittest.TestCase):
    def test_move_zeroes(self):
        self.assertEqual(move_zeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        self.assertEqual(move_zeroes([0, 0, 1]), [1, 0, 0])
        self.assertEqual(move_zeroes([0, 1, 0, 3, 12, 0, 0, 0, 0, 0]), [1, 3, 12, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeroes([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(move_zeroes([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])
