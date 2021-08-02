class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])

        result = False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    temp = helper(i, j, board, 0, word, visited)
                    if temp is True:
                        return True

        return False


def helper(x, y, board, pos, word, visited):
    m = len(board)
    n = len(board[0])

    if pos == len(word):
        return True

    if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited or board[x][y] != word[pos]:
        return False

    visited.add((x, y))

    temp1 = helper(x - 1, y, board, pos + 1, word, visited)
    temp2 = helper(x + 1, y, board, pos + 1, word, visited)
    temp3 = helper(x, y + 1, board, pos + 1, word, visited)
    temp4 = helper(x, y - 1, board, pos + 1, word, visited)

    visited.remove((x, y))

    return temp1 or temp2 or temp3 or temp4
