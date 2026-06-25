import unittest


class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        min_length_word = min(strs, key=len)
        res = []
        idx = 0

        for char in min_length_word:
            for text in strs:
                if text[idx] != char:
                    break
            else:
                res.append(char)
                idx += 1
        return "".join(res)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            (["flower", "flow", "flight"], "fl"),
            (["dog", "racecar", "car"], ""),
        ]

    def test_longest_common_prefix(self):
        for str, expected in self.test_cases:
            with self.subTest(str=str):
                self.assertEqual(self.solution.longest_common_prefix(str), expected)
