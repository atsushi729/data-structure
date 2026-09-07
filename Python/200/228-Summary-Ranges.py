import unittest


class Solution:
    def summary_ranges(self, nums: list[int]) -> list[str]:
        res = []

        if not nums:
            return res

        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{nums[i - 1]}")

                start = nums[i]

        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(f"{start}->{nums[-1]}")

        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.methods = [
            self.solution.summary_ranges
        ]

    def generate_test_cases(self):
        return [
            {
                "name": "Base Case",
                "nums": [0, 1, 2, 4, 5, 7],
                "expected": ["0->2", "4->5", "7"],
            },
            {
                "name": "Single Element",
                "nums": [1],
                "expected": ["1"],
            },
            {
                "name": "Empty Array",
                "nums": [],
                "expected": [],
            },
            {
                "name": "All Consecutive",
                "nums": [1, 2, 3, 4, 5],
                "expected": ["1->5"],
            },
            {
                "name": "No Consecutive Numbers",
                "nums": [1, 3, 5, 7],
                "expected": ["1", "3", "5", "7"],
            },
            {
                "name": "Negative Numbers",
                "nums": [-3, -2, -1, 1, 2],
                "expected": ["-3->-1", "1->2"],
            },
            {
                "name": "LeetCode Example 2",
                "nums": [0, 2, 3, 4, 6, 8, 9],
                "expected": ["0", "2->4", "6", "8->9"],
            },
        ]

    def test_summary_ranges(self):
        for method in self.methods:
            for case in self.generate_test_cases():
                with self.subTest(
                    method=method.__name__,
                    case=case["name"],
                ):
                    result = method(case["nums"])
                    self.assertEqual(result, case["expected"])
