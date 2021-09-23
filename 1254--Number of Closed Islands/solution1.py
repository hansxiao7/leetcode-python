class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def helper(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return True

            if grid[x][y] == 1 or grid[x][y] == -1:
                return False

            grid[x][y] = -1

            res = False
            for dx, dy in moves:
                temp = helper(x + dx, y + dy)
                res = res or temp
            return res

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    temp = helper(i, j)
                    if not temp:
                        result += 1
        return result



