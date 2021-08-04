import heapq


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dijkstra
        m = len(grid)
        n = len(grid[0])

        n_house = 0
        min_dis = [[[] for _ in range(n)] for _ in range(m)]
        next_pos = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    n_house += 1

                    # dijkstra
                    heap = [(0, i, j)]
                    visited = set()

                    while len(heap) != 0:
                        dis, x, y = heapq.heappop(heap)

                        if (x, y) in visited:
                            continue

                        visited.add((x, y))
                        min_dis[x][y].append(dis)

                        for k in range(4):
                            next_x = x + next_pos[k][0]
                            next_y = y + next_pos[k][1]

                            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or grid[next_x][next_y] != 0 or (
                            next_x, next_y) in visited:
                                continue

                            heapq.heappush(heap, (1 + dis, next_x, next_y))

        result = sys.maxint
        for i in range(m):
            for j in range(n):
                if len(min_dis[i][j]) == n_house and grid[i][j] == 0:
                    result = min(result, sum(min_dis[i][j]))

        if result == sys.maxint:
            return -1
        return result

