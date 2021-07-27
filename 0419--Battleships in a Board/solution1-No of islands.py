class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # 孤岛问题
        # DFS
        result = 0
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    result += 1
                    helper(board, i, j)

        return result


def helper(board, x, y):
    m = len(board)
    n = len(board[0])
    print(m, n)
    if x < 0 or x >= m or y < 0 or y >= n or board[x][y] == '.':
        return
    print(1)
    board[x][y] = '.'
    helper(board, x - 1, y)
    helper(board, x + 1, y)
    helper(board, x, y + 1)
    helper(board, x, y - 1)