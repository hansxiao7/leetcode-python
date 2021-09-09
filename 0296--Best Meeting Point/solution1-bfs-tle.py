class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dis = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    rank = 1
                    queue = [(i, j)]
                    visited = [[0 for _ in range(n)] for _ in range(m)]
                    visited[i][j] = 1

                    while len(queue) != 0:
                        n_q = len(queue)
                        for k in range(n_q):
                            x, y = queue.pop(0)

                            if x + 1 < m and visited[x + 1][y] == 0:
                                visited[x + 1][y] = 1
                                queue.append((x + 1, y))
                                dis[x + 1][y] += rank

                            if x - 1 >= 0 and visited[x - 1][y] == 0:
                                visited[x - 1][y] = 1
                                queue.append((x - 1, y))
                                dis[x - 1][y] += rank

                            if y + 1 < n and visited[x][y + 1] == 0:
                                visited[x][y + 1] = 1
                                queue.append((x, y + 1))
                                dis[x][y + 1] += rank

                            if y - 1 >= 0 and visited[x][y - 1] == 0:
                                visited[x][y - 1] = 1
                                queue.append((x, y - 1))
                                dis[x][y - 1] += rank

                        rank += 1

        res = sys.maxint
        for i in range(m):
            for j in range(n):
                if dis[i][j] < res:
                    res = dis[i][j]

        return res