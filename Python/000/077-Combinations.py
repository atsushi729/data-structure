import unittest


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        combinations = []

        def backtrack(start, current):
            if len(current) == k:
                combinations.append(current.copy())
                return

            for num in range(start, n + 1):
                current.append(num)
                backtrack(num + 1, current)
                current.pop()

        backtrack(1, [])
        return combinations


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

        self.methods = [
            self.solution.combine,
        ]

    def test_combine(self):
        test_cases = [
            {
                "name": "base case",
                "n": 4,
                "k": 2,
                "expected": [
                    [1, 2],
                    [1, 3],
                    [1, 4],
                    [2, 3],
                    [2, 4],
                    [3, 4],
                ],
            },
            {
                "name": "single element",
                "n": 1,
                "k": 1,
                "expected": [[1]],
            },
            {
                "name": "choose all elements",
                "n": 4,
                "k": 4,
                "expected": [[1, 2, 3, 4]],
            },
            {
                "name": "choose one element",
                "n": 3,
                "k": 1,
                "expected": [[1], [2], [3]],
            },
        ]

        for method in self.methods:
            for test_case in test_cases:
                with self.subTest(
                        method=method.__name__,
                        case=test_case["name"],
                ):
                    actual = method(
                        test_case["n"],
                        test_case["k"],
                    )

                    self.assertEqual(
                        actual,
                        test_case["expected"],
                    )
