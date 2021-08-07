class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])

        for x in range(k):
            temp = grid[m - 1][n - 1]
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if j == 0:
                        grid[i][j] = grid[i - 1][j - 1]
                    else:
                        grid[i][j] = grid[i][j - 1]
            grid[0][0] = temp

        return grid