import heapq


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        move = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        # bfs
        heap = [(1, 0, 0)]  # dis, x, y
        visited = set()

        n = len(grid)

        while len(heap) != 0:
            dis, x, y = heapq.heappop(heap)

            if (x, y) in visited or x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != 0:
                continue

            visited.add((x, y))

            if x == n - 1 and y == n - 1:
                return dis

            for dx, dy in move:

                new_x = x + dx
                new_y = y + dy
                if (new_x, new_y) not in visited:
                    heapq.heappush(heap, (dis + 1, new_x, new_y))

        return -1