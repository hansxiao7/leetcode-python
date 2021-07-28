class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        path = set()
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    temp = []
                    dfs(i, j, grid, temp)
                    path.add(tuple(temp))

        result = len(path)

        return result


def dfs(x, y, grid, path):
    m = len(grid)
    n = len(grid[0])

    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
        return

    grid[x][y] = 0

    path.append((-1, 0))
    dfs(x - 1, y, grid, path)

    path.append((1, 0))
    dfs(x + 1, y, grid, path)

    path.append((0, -1))
    dfs(x, y - 1, grid, path)

    path.append((0, 1))
    dfs(x, y + 1, grid, path)