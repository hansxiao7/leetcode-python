class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        left = [[0 for _ in range(n)] for _ in range(m)]
        right = [[0 for _ in range(n)] for _ in range(m)]
        up = [[0 for _ in range(n)] for _ in range(m)]
        down = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if j != 0:
                    if grid[i][j - 1] == '0':
                        left[i][j] = left[i][j - 1]
                    elif grid[i][j - 1] == 'E':
                        left[i][j] = left[i][j - 1] + 1
                    else:
                        left[i][j] = 0

                if i != 0:
                    if grid[i - 1][j] == '0':
                        up[i][j] = up[i - 1][j]
                    elif grid[i - 1][j] == 'E':
                        up[i][j] = up[i - 1][j] + 1
                    else:
                        up[i][j] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i != m - 1:
                    if grid[i + 1][j] == '0':
                        down[i][j] = down[i + 1][j]
                    elif grid[i + 1][j] == 'E':
                        down[i][j] = down[i + 1][j] + 1
                    else:
                        down[i][j] = 0

                if j != n - 1:
                    if grid[i][j + 1] == '0':
                        right[i][j] = right[i][j + 1]
                    elif grid[i][j + 1] == 'E':
                        right[i][j] = right[i][j + 1] + 1
                    else:
                        right[i][j] = 0

        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res = max(res, left[i][j] + up[i][j] + right[i][j] + down[i][j])

        return res