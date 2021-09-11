class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]

        self.res = 0

        def helper(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                self.res += 1
                return

            if visited[x][y] == 1:
                return

            visited[x][y] = 1
            helper(x + 1, y)
            helper(x - 1, y)
            helper(x, y + 1)
            helper(x, y - 1)

        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    helper(i, j)

        return self.res