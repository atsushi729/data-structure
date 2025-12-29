import unittest
from typing import List


class Solution:
    def cal_points(self, operations: List[str]) -> int:
        """
        Time complexity: O(N) where N is the length of operations
        Space complexity: O(N) where N is the length of operations
        """
        stack = []

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)

    def cal_points_v2(self, operations: List[str]) -> int:
        """
        Time complexity: O(N) where N is the length of operations
        Space complexity: O(N) where N is the length of operations
        """
        res = []

        for op in operations:
            if op == "+":
                prev_1 = res[-1]
                prev_2 = res[-2]
                res.append(prev_1 + prev_2)
            elif op == "D":
                prev_1 = res[-1]
                res.append(prev_1 * 2)
            elif op == "C":
                res.pop()
            else:
                res.append(int(op))
        return sum(res)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            (["5", "2", "C", "D", "+"], 30),
            (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
            (["1"], 1),
        ]

    def test_cal_points(self):
        for operations, expected in self.test_cases:
            with self.subTest(operations=operations, expected=expected):
                self.assertEqual(self.s.cal_points(operations), expected)

    def test_cal_points_v2(self):
        for operations, expected in self.test_cases:
            with self.subTest(operations=operations, expected=expected):
                self.assertEqual(self.s.cal_points_v2(operations), expected)
