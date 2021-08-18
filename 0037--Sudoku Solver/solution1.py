class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = {}
        col = {}
        box = {}

        for i in range(9):
            row[i] = set()
            for j in range(9):
                if board[i][j] != '.':
                    row[i].add(int(board[i][j]))

        for j in range(9):
            col[j] = set()
            for i in range(9):
                if board[i][j] != '.':
                    col[j].add(int(board[i][j]))

        for i in range(3):
            for j in range(3):
                box[(i, j)] = set()
                for m in range(3):
                    for n in range(3):
                        ele = board[3 * i + m][3 * j + n]
                        if ele != '.':
                            box[(i, j)].add(int(ele))

        def helper(x, y):
            total = 0
            for i in range(9):
                total += len(row[i])
            if total == 9 * 9:
                return True

            next_row, next_col = (x, y + 1) if y != 8 else (x + 1, 0)

            if board[x][y] != '.':
                return helper(next_row, next_col)

            result = False
            box_id = (x // 3, y // 3)
            for num in range(1, 10):
                if num not in box[box_id] and num not in col[y] and num not in row[x]:
                    box[box_id].add(num)
                    col[y].add(num)
                    row[x].add(num)
                    result = result or helper(next_row, next_col)
                    if result:
                        board[x][y] = str(num)
                        return True
                    box[box_id].remove(num)
                    col[y].remove(num)
                    row[x].remove(num)

            return False

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    helper(i, j)
                    break
        return board




