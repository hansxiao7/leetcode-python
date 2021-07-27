class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        result = 0
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    result += 1

                    if i != 0 and board[i - 1][j] == 'X':  # vertical
                        result -= 1
                    if j != 0 and board[i][j - 1] == 'X':  # horizontal
                        result -= 1

        return result
