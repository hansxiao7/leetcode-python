class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        # put in queue
        visited = [[0 for _ in range(n)] for _ in range(m)]
        queue = collections.deque()
        neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def helper(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                return

            queue.append((x, y))
            grid[x][y] = -1
            visited[x][y] = 1

            for dx, dy in neighbors:
                helper(x + dx, y + dy)

        flag = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    helper(i, j)
                    flag = True
                    break
            if flag:
                break

        rank = 0

        while len(queue) != 0:
            n_q = len(queue)
            for i in range(n_q):
                x, y = queue.popleft()

                for dx, dy in neighbors:
                    newX = x + dx
                    newY = y + dy
                    if newX < 0 or newX >= m or newY < 0 or newY >= n:
                        continue

                    if visited[newX][newY] == 0:
                        visited[newX][newY] = 1
                        if grid[newX][newY] == 0:
                            queue.append((newX, newY))
                        elif grid[newX][newY] == 1:
                            return rank
            rank += 1



