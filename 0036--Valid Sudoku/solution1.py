class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = []
        column = []
        box = [[0 for _ in range(3)] for _ in range(3)]

        m = len(board)
        n = len(board[0])

        for i in range(m):
            temp = 0
            for j in range(n):
                if board[i][j] != '.':
                    curr = board[i][j]
                    if temp == temp | 1 << int(curr):
                        return False
                    temp |= 1 << int(board[i][j])
            row.append(temp)

        for j in range(n):
            temp = 0
            for i in range(m):
                if board[i][j] != '.':
                    curr = board[i][j]
                    if temp == temp | 1 << int(curr):
                        return False
                    temp |= 1 << int(board[i][j])
            column.append(temp)

        for i in range(3):
            for j in range(3):
                temp = 0
                for m in range(3):
                    for n in range(3):
                        curr = board[i * 3 + m][j * 3 + n]
                        if curr != '.':
                            if temp == temp | 1 << int(curr):
                                return False
                            temp |= 1 << int(curr)
                box[i][j] = temp

        return True