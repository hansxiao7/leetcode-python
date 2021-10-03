import heapq


class Solution(object):
    def maximumMinimumPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        queue = [(-grid[0][0], 0, 0)]
        visited = [[0 for _ in range(n)] for _ in range(m)]
        res = sys.maxint
        visited[0][0] = 1

        neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while len(queue) != 0:
            val, x, y = heapq.heappop(queue)

            res = min(res, -val)

            if x == m - 1 and y == n - 1:
                return res

            for dx, dy in neighbors:
                if x + dx < 0 or x + dx >= m or y + dy < 0 or y + dy >= n or visited[x + dx][y + dy] == 1:
                    continue

                visited[x + dx][y + dy] = 1

                heapq.heappush(queue, (-grid[x + dx][y + dy], x + dx, y + dy))

