class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    result += 1
                    helper(grid, i, j)

        return result


def helper(grid, x, y):
    m = len(grid)
    n = len(grid[0])
    if x < 0 or x > m - 1 or y < 0 or y > n - 1 or grid[x][y] == '0':
        return

    if grid[x][y] == '1':
        grid[x][y] = '0'
        helper(grid, x - 1, y)
        helper(grid, x + 1, y)
        helper(grid, x, y - 1)
        helper(grid, x, y + 1)


