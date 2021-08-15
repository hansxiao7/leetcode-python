class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m = len(board)
        n = len(board[0])

        pos = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        # BFS
        queue = collections.deque()
        queue.append(click)
        visited = set()
        while len(queue) != 0:
            x, y = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            n_mine = 0
            temp = []
            for p in pos:
                new_x = x + p[0]
                new_y = y + p[1]

                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                    if board[new_x][new_y] == 'M':
                        n_mine += 1
                    elif board[new_x][new_y] == 'E' and (new_x, new_y) not in visited:
                        temp.append((new_x, new_y))

            if n_mine == 0:
                board[x][y] = 'B'
                queue.extend(temp)
            else:
                board[x][y] = str(n_mine)

        return board
