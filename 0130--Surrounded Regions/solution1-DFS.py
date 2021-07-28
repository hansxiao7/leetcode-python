class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            dfs(i, 0, board)
            dfs(i, n - 1, board)

        for i in range(n):
            dfs(0, i, board)
            dfs(m - 1, i, board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'G':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        return board


def dfs(x, y, board):
    m = len(board)
    n = len(board[0])
    if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O':
        return

    board[x][y] = 'G'
    dfs(x - 1, y, board)
    dfs(x + 1, y, board)
    dfs(x, y - 1, board)
    dfs(x, y + 1, board)