class Solution:
    def isValidSudoku(self, board: list):
        ## check each row
        for row in board:
            if not self.isValidUnit(row):
                return False

        ## Check each column
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.isValidUnit(column):
                return False

        ## Check each sub-box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subBox = [board[row][col] for row in range(i, 1 + 3) for col in range(j, j + 3)]
                if not self.isValidUnit(subBox):
                    return False

        return True

    def isValidUnit(self, unit: list) -> bool:
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]
         ]

if __name__ == "__main__":
    s = Solution()
    s.isValidSudoku(board)
    if s.isValidSudoku(board):
        print('ok')
