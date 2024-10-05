#################### Solution ####################
import unittest


def is_valid_sudoku(board: list[list[str]]) -> bool:
    # Check rows
    for i in range(9):
        filtered_row = [x for x in board[i] if x != '.']
        if len(filtered_row) != len(set(filtered_row)):
            return False

    # Check columns
    for i in range(9):
        filtered_col = [board[j][i] for j in range(9) if board[j][i] != '.']
        if len(filtered_col) != len(set(filtered_col)):
            return False

    # Check 3x3 sub-boxes
    for box_row in range(3):
        for box_col in range(3):
            sub_box = []
            for i in range(3):
                for j in range(3):
                    val = board[3 * box_row + i][3 * box_col + j]
                    if val != '.':
                        sub_box.append(val)
            if len(sub_box) != len(set(sub_box)):
                return False

    # All checks passed
    return True


def is_valid_sudoku_model(board: list[list[str]]) -> bool:
    # 各行、列、サブボックスのセットを初期化
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    squares = [set() for _ in range(9)]  # サブボックスは0〜8のインデックス

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == ".":
                continue  # 空のセルはスキップ

            # サブボックスのインデックスを計算
            square_index = (r // 3) * 3 + (c // 3)

            # 行、列、サブボックスでの重複をチェック
            if (
                    num in rows[r]
                    or num in cols[c]
                    or num in squares[square_index]
            ):
                # 重複が見つかった場合は無効
                return False

            # 重複がなければ、それぞれのセットに追加
            rows[r].add(num)
            cols[c].add(num)
            squares[square_index].add(num)

    # 全てのチェックをパスした場合は有効
    return True
