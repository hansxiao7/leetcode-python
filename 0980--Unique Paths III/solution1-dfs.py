class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    visited.add((i, j))

                if grid[i][j] == 1:
                    start_x = i
                    start_y = j

        self.result = 0

        def dfs(x, y, grid, visited):
            m = len(grid)
            n = len(grid[0])

            if (x, y) in visited:
                return

            visited.add((x, y))
            if grid[x][y] == 2:
                if len(visited) == m * n:
                    self.result += 1
                visited.remove((x, y))
                return

            if x - 1 >= 0:
                if (x - 1, y) not in visited:
                    dfs(x - 1, y, grid, visited)

            if x + 1 < m:
                if (x + 1, y) not in visited:
                    dfs(x + 1, y, grid, visited)

            if y - 1 >= 0:
                if (x, y - 1) not in visited:
                    dfs(x, y - 1, grid, visited)

            if y + 1 < n:
                if (x, y + 1) not in visited:
                    dfs(x, y + 1, grid, visited)

            visited.remove((x, y))

        dfs(start_x, start_y, grid, visited)

        return self.result