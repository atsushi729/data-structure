import unittest
from collections import Counter


class Solution:
    def min_window(self, s: str, t: str) -> str:
        if not t:
            return ""

        # tに含まれる各文字の必要な出現回数をカウント
        required_char_counts = {}
        for char in t:
            required_char_counts[char] = required_char_counts.get(char, 0) + 1

        # 現在のウィンドウ内の文字の出現回数をカウント
        window_char_counts = {}

        # 現在のウィンドウが満たしている条件
        formed_chars = 0
        required_unique_chars = len(required_char_counts)

        # 最小ウィンドウの情報を保持する変数
        min_window_range = [-1, -1]
        min_window_length = float("infinity")

        # スライディングウィンドウの左端ポインタ
        left_pointer = 0

        # スライディングウィンドウの右端ポインタを0から開始
        for right_pointer in range(len(s)):
            current_char = s[right_pointer]
            window_char_counts[current_char] = window_char_counts.get(current_char, 0) + 1

            # 現在の文字がtに含まれ、必要な回数に達した場合
            if current_char in required_char_counts and window_char_counts[current_char] == required_char_counts[
                current_char]:
                formed_chars += 1

            # ウィンドウが条件を満たしている間、左端を縮小
            while formed_chars == required_unique_chars:
                window_size = right_pointer - left_pointer + 1
                if window_size < min_window_length:
                    min_window_length = window_size
                    min_window_range = [left_pointer, right_pointer]

                # 左端の文字をウィンドウから除去
                left_char = s[left_pointer]
                window_char_counts[left_char] -= 1

                # 除去した文字がtに含まれ、必要な回数を下回った場合
                if left_char in required_char_counts and window_char_counts[left_char] < required_char_counts[
                    left_char]:
                    formed_chars -= 1

                # 左端ポインタを右に移動
                left_pointer += 1

        # 最小ウィンドウが見つかった場合、その部分文字列を返す
        start, end = min_window_range
        if min_window_length != float("infinity"):
            return s[start:end + 1]
        else:
            return ""

    def min_window_v2(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res, resLen = [-1, -1], float("infinity")
        for i in range(len(s)):
            countS = {}
            for j in range(i, len(s)):
                countS[s[j]] = 1 + countS.get(s[j], 0)

                flag = True
                for c in countT:
                    if countT[c] > countS.get(c, 0):
                        flag = False
                        break

                if flag and (j - i + 1) < resLen:
                    resLen = j - i + 1
                    res = [i, j]

        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""

    def min_window_v3(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        target = Counter(t)
        window = {}

        have = 0
        need = len(target)

        res_start = 0
        res_len = float("inf")

        left = 0
        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            if char in target and window[char] == target[char]:
                have += 1

            while have == need:
                window_len = right - left + 1
                if window_len < res_len:
                    res_start = left
                    res_len = window_len

                left_char = s[left]
                window[left_char] -= 1
                if left_char in target and window[left_char] < target[left_char]:
                    have -= 1
                left += 1

        return "" if res_len == float("inf") else s[res_start:res_start + res_len]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("ADOBECODEBANC", "ABC", "BANC"),
            ("a", "a", "a"),
            ("a", "aa", ""),
            ("ab", "A", ""),
            ("aaflslflsldkalskaaa", "aaa", "aaa"),
        ]

    def test_min_window(self):
        for s, t, expected in self.test_cases:
            self.assertEqual(self.solution.min_window(s, t), expected)

    def test_min_window_v2(self):
        for s, t, expected in self.test_cases:
            self.assertEqual(self.solution.min_window_v2(s, t), expected)

    def test_min_window_v3(self):
        for s, t, expected in self.test_cases:
            self.assertEqual(self.solution.min_window_v3(s, t), expected)
