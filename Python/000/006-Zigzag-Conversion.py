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

    def convert_v3(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = []
        for r in range(numRows):
            increment = 2 * (numRows - 1)

            for i in range(r, len(s), increment):
                res.append(s[i])
                if 0 < r < numRows - 1 and i + increment - 2 * r < len(s):
                    res.append(s[i + increment - 2 * r])

        return "".join(res)


###################### Test Case ####################
###################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.methods = [
            cls.solution.convert,
            cls.solution.convert_v2,
            cls.solution.convert_v3,
        ]

        cls.test_cases = [
            ("AAB", 2, "ABA"),
            ("AAAAB", 3, "ABAAA"),
            ("AABAAB", 4, "AABBAA"),
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
            ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
            ("ABCDE", 2, "ACEBD"),
            ("ABCDE", 3, "AEBDC"),
            ("ABCDE", 1, "ABCDE"),
            ("ABCDE", 5, "ABCDE"),
            ("ABCDE", 10, "ABCDE"),
            ("A", 1, "A"),
            ("A", 2, "A"),
            ("", 1, ""),
            ("", 3, ""),
        ]

    def test_convert(self):
        for method in self.methods:
            for s, numRows, expected in self.test_cases:
                with self.subTest(
                        method=method.__name__,
                        s=s,
                        numRows=numRows
                ):
                    self.assertEqual(
                        method(s, numRows),
                        expected
                    )
