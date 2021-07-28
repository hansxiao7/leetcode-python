class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        board = grid
        m = len(board)
        n = len(board[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    result = max(result, dfs(i, j, board))

        return result


def dfs(x, y, board):
    m = len(board)
    n = len(board[0])
    if x < 0 or x >= m or y < 0 or y >= n or board[x][y] == 0:
        return 0

    board[x][y] = 0

    result = 1 + dfs(x - 1, y, board) + dfs(x + 1, y, board) + dfs(x, y - 1, board) + dfs(x, y + 1, board)

    return result