import unittest


class Solution:
    def remove_element(self, nums: list[int], val: int) -> int:
        write_index = 0

        for num in nums:
            if num != val:
                nums[write_index] = num
                write_index += 1

        return write_index

    def remove_element_v2(self, nums: list[int], val: int) -> int:
        current_index = len(nums) - 1

        while current_index >= 0:
            if nums[current_index] == val:
                nums.pop(current_index)
            current_index -= 1

        return len(nums)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ([3, 2, 2, 3], 3, [2, 2]),
            ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]),
            ([1, 2, 3], 4, [1, 2, 3]),
            ([1, 1, 1], 1, []),
            ([], 1, []),
        ]

    def test_remove_element(self):
        for nums, val, expected in self.test_cases:
            with self.subTest(nums=nums, val=val):
                nums_copy = nums.copy()

                length = self.solution.remove_element(nums_copy, val)

                self.assertEqual(nums_copy[:length], expected)
                self.assertEqual(length, len(expected))

    def test_remove_element_v2(self):
        for nums, val, expected in self.test_cases:
            with self.subTest(nums=nums, val=val):
                nums_copy = nums.copy()

                length = self.solution.remove_element_v2(nums_copy, val)

                self.assertEqual(nums_copy[:length], expected)
                self.assertEqual(length, len(expected))


if __name__ == "__main__":
    unittest.main()