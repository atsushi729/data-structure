import unittest


def longestConsecutive(nums: list[int]) -> int:
    sorted_nums = sorted(set(nums))
    if not sorted_nums:
        return 0

    max_consecutive = 1
    current_consecutive = 1

    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i - 1] + 1:
            current_consecutive += 1
        else:
            max_consecutive = max(max_consecutive, current_consecutive)
            current_consecutive = 1

    return max(max_consecutive, current_consecutive)


class TestLongestConsecutive(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([100, 4, 200, 1, 3, 2], 4),
            ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
            ([], 0),
            ([1], 1),
            ([1, 2, 0, 1], 3),
            ([10, 10, 10], 1),
        ]

    def test_longest_consecutive(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                actual = longestConsecutive(nums)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
