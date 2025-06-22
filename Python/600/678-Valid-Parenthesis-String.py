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

    def check_valid_string2(self, s: str) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        left, star = [], []

        for i, char in enumerate(s):
            if char == '(':
                left.append(i)
            elif char == '*':
                star.append(i)
            else:  # char == ')'
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while left and star:
            if left[-1] < star[-1]:
                left.pop()
                star.pop()
            else:
                return False

        return not left


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

    def test_checkValidString2(self):
        for s, expected in self.test_cases:
            with self.subTest(s=s, expected=expected):
                result = self.solution.check_valid_string2(s)
                self.assertEqual(result, expected)
