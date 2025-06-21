import unittest


class Solution:
    def check_valid_string(self, s: str) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        left_min, right_max = 0, 0

        for char in s:
            if char == '(':
                left_min += 1
                right_max += 1
            elif char == ')':
                left_min -= 1
                right_max -= 1
            else:
                left_min -= 1
                right_max += 1
            if right_max < 0:
                return False
            if left_min < 0:
                left_min = 0
        return left_min == 0


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("()", True),
            ("(*)", True),
            ("(*))", True),
            ("((*)", True),
            ("(())((())()()(*)(*()(())())())()()((()())((()))(*", False),
            (")(", False),
            ("*", True),
        ]

    def test_checkValidString(self):
        for s, expected in self.test_cases:
            with self.subTest(s=s, expected=expected):
                result = self.solution.check_valid_string(s)
                self.assertEqual(result, expected)
