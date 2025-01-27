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


###################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_convert(self):
        solution = Solution()
        self.assertEqual(solution.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(solution.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        self.assertEqual(solution.convert("A", 1), "A")
