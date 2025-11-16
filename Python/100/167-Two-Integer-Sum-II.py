import unittest


#################### Solution ####################
class Solution:
    def two_sum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(0, len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

    def two_sum_v2(self, numbers: list[int], target: int) -> list[int]:
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

    def two_sum_v3(self, numbers: list[int], target: int) -> list[int]:
        num_dict = {}

        for i, num in enumerate(numbers):
            complement = target - num

            if complement in num_dict:
                return [num_dict[complement] + 1, i + 1]

            num_dict[num] = i

        return []


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        self.test_cases = [
            # (numbers, target, expected)
            ([2, 7, 11, 15], 9, [1, 2]),
            ([2, 3, 4], 6, [1, 3]),
            ([-1, 0], -1, [1, 2]),
        ]

    def test_two_sum(self):
        for numbers, target, expected in self.test_cases:
            with self.subTest(numbers=numbers, target=target):
                result = self.s.two_sum(numbers, target)
                self.assertEqual(result, expected)

    def test_model_two_sum(self):
        for numbers, target, expected in self.test_cases:
            with self.subTest(numbers=numbers, target=target):
                result = self.s.two_sum_v2(numbers, target)
                self.assertEqual(result, expected)

    def test_two_sum_v3(self):
        for numbers, target, expected in self.test_cases:
            with self.subTest(numbers=numbers, target=target):
                result = self.s.two_sum_v3(numbers, target)
                self.assertEqual(result, expected)
