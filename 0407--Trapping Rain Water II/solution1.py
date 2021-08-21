import heapq


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m = len(heightMap)
        n = len(heightMap[0])

        heap = []
        visited = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(1, n - 1):
            heapq.heappush(heap, (heightMap[0][i], 0, i))
            visited[0][i] = 1
            heapq.heappush(heap, (heightMap[m - 1][i], m - 1, i))
            visited[m - 1][i] = 1

        for i in range(1, m - 1):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            visited[i][0] = 1
            heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][n - 1] = 1

        visited[0][0] = 1
        visited[m - 1][0] = 1
        visited[0][n - 1] = 1
        visited[m - 1][n - 1] = 1

        move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        result = 0

        while len(heap) != 0:
            h, x, y = heapq.heappop(heap)
            for dx, dy in move:
                new_x = x + dx
                new_y = y + dy

                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or visited[new_x][new_y] == 1:
                    continue

                visited[new_x][new_y] = 1

                if heightMap[new_x][new_y] < h:
                    result += h - heightMap[new_x][new_y]
                    heapq.heappush(heap, (h, new_x, new_y))
                else:
                    heapq.heappush(heap, (heightMap[new_x][new_y], new_x, new_y))

        return result
