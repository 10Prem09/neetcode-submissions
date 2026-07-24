class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                value = int(board[i][j]) - 1
                if 1 << value & rows[i]:
                    return False
                if 1 << value & cols[j]:
                    return False
                if 1 << value & squares[(i//3)*3 + (j//3)]:
                    return False
                rows[i] |= 1 << value
                cols[j] |= 1 << value
                squares[(i//3)*3 + (j//3)] |= 1 << value
        return True
