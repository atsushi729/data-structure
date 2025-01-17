from typing import List
import unittest


#################### Solution ####################
class Solution:
    def letter_combinations(self, digits: str) -> List[str]:
        # Input validation
        if not digits:
            return []

        res = [""]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        for digit in digits:
            tmp = []
            for r in res:
                for char in digitToChar[digit]:
                    tmp.append(r + char)
            res = tmp

        return res

    def letter_combinations(self, digits: str) -> List[str]:
        # Input validation
        if not digits:
            return []

        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, cur_str):
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return

            for c in digitToChar[digits[i]]:
                backtrack(i + 1, cur_str + c)

        if digits:
            backtrack(0, "")

        return res


##################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_letter_combinations(self):
        solution = Solution()
        self.assertListEqual(solution.letter_combinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        self.assertListEqual(solution.letter_combinations(""), [])
        self.assertListEqual(solution.letter_combinations("2"), ["a", "b", "c"])

    def test_letter_combinations_v2(self):
        solution = Solution()
        self.assertListEqual(solution.letter_combinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        self.assertListEqual(solution.letter_combinations(""), [])
        self.assertListEqual(solution.letter_combinations("2"), ["a", "b", "c"])
