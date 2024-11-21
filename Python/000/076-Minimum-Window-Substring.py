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
