class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        matrix = [[1 for _ in range(n)] for _ in range(n)]
        for x, y in mines:
            matrix[x][y] = 0

        up = [[0] * (n) for _ in range(n)]
        down = [[0] * (n) for _ in range(n)]
        left = [[0] * (n) for _ in range(n)]
        right = [[0] * (n) for _ in range(n)]

        for i in range(n):
            for j in range(n):
                # left and up
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    left[i][j] = (left[i][j - 1] + 1) * (matrix[i][j - 1] == 1)
                elif j == 0:
                    up[i][j] = (up[i - 1][j] + 1) * (matrix[i - 1][j] == 1)
                else:
                    left[i][j] = (left[i][j - 1] + 1) * (matrix[i][j - 1] == 1)
                    up[i][j] = (up[i - 1][j] + 1) * (matrix[i - 1][j] == 1)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == n - 1 and j == n - 1:
                    continue
                elif i == n - 1:
                    right[i][j] = (right[i][j + 1] + 1) * (matrix[i][j + 1] == 1)
                elif j == n - 1:
                    down[i][j] = (down[i + 1][j] + 1) * (matrix[i + 1][j] == 1)
                else:
                    right[i][j] = (right[i][j + 1] + 1) * (matrix[i][j + 1] == 1)
                    down[i][j] = (down[i + 1][j] + 1) * (matrix[i + 1][j] == 1)

        res = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    temp = 1 + min(left[i][j], up[i][j], down[i][j], right[i][j])
                    res = max(res, temp)

        return res