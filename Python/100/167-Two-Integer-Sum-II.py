import unittest


#################### Solution ####################
def two_sum(numbers: list[int], target: int) -> list[int]:
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]


def model_two_sum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1

    return []


#################### Test Case ####################
class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [1, 2])

    def test_two_sum_v1(self):
        self.assertEqual(two_sum([2, 3, 4], 6), [1, 3])

    def test_two_sum_v2(self):
        self.assertEqual(two_sum([-1, 0], -1), [1, 2])

    def test_model_two_sum(self):
        self.assertEqual(model_two_sum([2, 7, 11, 15], 9), [1, 2])
