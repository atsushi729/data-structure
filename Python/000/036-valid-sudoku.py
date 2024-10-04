def isValidSudoku(board: list[list[str]]) -> bool:
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


board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
         ["4", ".", ".", "5", ".", ".", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", ".", "3"],
         ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
         [".", ".", ".", "8", ".", "3", ".", ".", "5"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", ".", ".", ".", ".", ".", "2", ".", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "8"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(isValidSudoku(board))
