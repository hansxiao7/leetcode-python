class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # DFS
        m = len(grid)
        n = len(grid[0])

        dis = [[sys.maxint for _ in range(n)] for _ in range(m)]
        food_pos = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    x = i
                    y = j
                    break

        result = []
        dis[x][y] = 0

        dfs(x, y, grid, dis, result)
        if len(result) == 0:
            return -1
        else:
            return min(result)


def dfs(x, y, grid, dis, result):
    m = len(grid)
    n = len(grid[0])

    if grid[x][y] == '#':
        result.append(dis[x][y])
        return

    if x - 1 >= 0 and grid[x - 1][y] != 'X':
        if dis[x - 1][y] > dis[x][y] + 1:
            dis[x - 1][y] = dis[x][y] + 1
            dfs(x - 1, y, grid, dis, result)
    if x + 1 < m and grid[x + 1][y] != 'X':
        if dis[x + 1][y] > dis[x][y] + 1:
            dis[x + 1][y] = dis[x][y] + 1
            dfs(x + 1, y, grid, dis, result)
    if y - 1 >= 0 and grid[x][y - 1] != 'X':
        if dis[x][y - 1] > dis[x][y] + 1:
            dis[x][y - 1] = dis[x][y] + 1
            dfs(x, y - 1, grid, dis, result)

    if y + 1 < n and grid[x][y + 1] != 'X':
        if dis[x][y + 1] > dis[x][y] + 1:
            dis[x][y + 1] = dis[x][y] + 1
            dfs(x, y + 1, grid, dis, result)