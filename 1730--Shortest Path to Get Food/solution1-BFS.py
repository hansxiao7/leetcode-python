class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # BFS
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    x = i
                    y = j
                    break

        dis = [[sys.maxint for _ in range(n)] for _ in range(m)]
        dis[x][y] = 0

        queue = [[x, y]]

        while len(queue) != 0:
            node = queue.pop(0)
            x_curr = node[0]
            y_curr = node[1]

            if grid[x_curr][y_curr] == '#':
                return dis[x_curr][y_curr]

            if x_curr - 1 >= 0:
                if grid[x_curr - 1][y_curr] != 'X' and dis[x_curr - 1][y_curr] > dis[x_curr][y_curr] + 1:
                    dis[x_curr - 1][y_curr] = dis[x_curr][y_curr] + 1
                    queue.append([x_curr - 1, y_curr])
            if x_curr + 1 < m:
                if grid[x_curr + 1][y_curr] != 'X' and dis[x_curr + 1][y_curr] > dis[x_curr][y_curr] + 1:
                    dis[x_curr + 1][y_curr] = dis[x_curr][y_curr] + 1
                    queue.append([x_curr + 1, y_curr])
            if y_curr - 1 >= 0:
                if grid[x_curr][y_curr - 1] != 'X' and dis[x_curr][y_curr - 1] > dis[x_curr][y_curr] + 1:
                    dis[x_curr][y_curr - 1] = dis[x_curr][y_curr] + 1
                    queue.append([x_curr, y_curr - 1])
            if y_curr + 1 < n:
                if grid[x_curr][y_curr + 1] != 'X' and dis[x_curr][y_curr + 1] > dis[x_curr][y_curr] + 1:
                    dis[x_curr][y_curr + 1] = dis[x_curr][y_curr] + 1
                    queue.append([x_curr, y_curr + 1])

        return -1
