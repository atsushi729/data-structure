import unittest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        cur_row = 0
        going_down = False

        for char in s:
            rows[cur_row] += char
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1

        return "".join(rows)

    def convert_v2(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ["" for _ in range(numRows)]
        index = 0
        step = 1

        for char in s:
            rows[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return "".join(rows)


###################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("AAB", 2, "ABA"),
            ("AAAAB", 3, "ABAAA"),
            ("AABAAB", 4, "AABBAA"),
        ]

    def test_convert(self):
        for s, numRows, expectet in self.test_cases:
            with self.subTest(s=s, numRows=numRows):
                self.assertEqual(self.solution.convert(s, numRows), expectet)

    def test_convert_v2(self):
        for s, numRows, expectet in self.test_cases:
            with self.subTest(s=s, numRows=numRows):
                self.assertEqual(self.solution.convert_v2(s, numRows), expectet)
