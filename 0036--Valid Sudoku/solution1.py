class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [0 for _ in range(9)]
        col = [0 for _ in range(9)]
        box = [[0 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    temp = 1 << int(board[i][j])

                    if row[i] | temp == row[i] or col[j] | temp == col[j] or box[i // 3][j // 3] | temp == box[i // 3][
                        j // 3]:
                        return False

                    row[i] |= temp
                    col[j] |= temp
                    box[i // 3][j // 3] |= temp

        return True