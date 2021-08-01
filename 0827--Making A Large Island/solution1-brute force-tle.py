class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        visited = set()

        self.result = 0

        def dfs(x, y, grid, visited):
            n = len(grid)
            if x < 0 or x >= n or y < 0 or y >= n or (x, y) in visited or grid[x][y] != 1:
                self.result = max(self.result, len(visited))
                return

            visited.add((x, y))

            dfs(x - 1, y, grid, visited)
            dfs(x + 1, y, grid, visited)
            dfs(x, y - 1, grid, visited)
            dfs(x, y + 1, grid, visited)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    visited = set()
                    grid[i][j] = 1
                    dfs(i, j, grid, visited)
                    grid[i][j] = 0

        if self.result == 0:
            return n * n

        return self.result


