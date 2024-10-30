import unittest


class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


#################### Test Case ####################
class TestEncodeAndDecodeString(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(Solution().encode(["hello", "world"]), "5#hello5#world")
        self.assertEqual(Solution().encode(["a", "b", "c"]), "1#a1#b1#c")

    def test_decode(self):
        self.assertEqual(Solution().decode("5#hello5#world"), ["hello", "world"])
        self.assertEqual(Solution().decode("1#a1#b1#c"), ["a", "b", "c"])
