import unittest


class Solution:
    def full_justify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            if length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1
            else:
                extra_space = maxWidth - length
                remainder = extra_space % max(1, len(line) - 1)
                space = extra_space // max(1, len(line) - 1)
                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * space
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                res.append("".join(line))
                line, length = [], 0

        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + " " * trail_space)
        return res


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            (["This", "is", "an", "example", "of", "text", "justification."], 16, [
                "This    is    an",
                "example  of text",
                "justification.  "
            ]),
            (["What", "must", "be", "acknowledgment", "shall", "be"], 16, [
                "What   must   be",
                "acknowledgment  ",
                "shall be        "
            ]),
            (["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
              "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20, [
                 "Science  is  what we",
                 "understand      well",
                 "enough to explain to",
                 "a  computer.  Art is",
                 "everything  else  we",
                 "do                  "
             ])

        ]

    def test_full_justify(self) -> None:
        for words, maxWidth, expected in self.test_cases:
            with self.subTest(words=words, maxWidth=maxWidth):
                self.assertEqual(self.solution.full_justify(words, maxWidth), expected)
