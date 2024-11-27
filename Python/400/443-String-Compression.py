import unittest


#################### Solution ####################
class Solution:
    def compress(self, chars: list[str]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        write = 0  # 書き込みポインタ
        read = 0  # 読み込みポインタ
        n = len(chars)

        while read < n:
            current_char = chars[read]
            count = 0

            # 現在の文字の連続数をカウント
            while read < n and chars[read] == current_char:
                read += 1
                count += 1

            # 文字を配置
            chars[write] = current_char
            write += 1

            # カウントが1より大きい場合、数字を文字列として配置
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write


#################### Test Case ####################
class TestCompress(unittest.TestCase):
    def test_compress(self):
        self.assertEqual(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]), 6)
        self.assertEqual(Solution().compress(["a", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"]), 5)
        self.assertEqual(Solution().compress(["a", "a", "b", "b", "c", "c", "c", "d", "d", "d"]), 8)
