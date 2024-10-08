import unittest


#################### Solution ####################
def two_sum(self, numbers: list[int], target: int) -> list[int]:
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]


#################### Test Case ####################
class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [1, 2])

    def test_two_sum_v1(self):
        self.assertEqual(two_sum([2, 3, 4], 6), [1, 3])

    def test_two_sum_v2(self):
        self.assertEqual(two_sum([-1, 0], -1), [1, 2])

    def test_two_sum_v3(self):
        self.assertEqual(two_sum([1, 2, 5, 6, 3], 9), [2, 4])
