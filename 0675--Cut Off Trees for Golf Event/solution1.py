class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if forest[0][0] == 0:
            return -1

        m = len(forest)
        n = len(forest[0])

        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))

        trees.sort(key=lambda x: -x[0])

        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(x, y, targetX, targetY):
            queue = collections.deque()
            visited = [[0 for _ in range(n)] for _ in range(m)]
            queue.append((x, y))

            visited[x][y] = 1
            step = 0

            while len(queue) != 0:
                n_q = len(queue)

                for i in range(len(queue)):
                    posX, posY = queue.popleft()
                    if posX == targetX and posY == targetY:
                        return step
                    for dx, dy in neighbors:
                        newX = posX + dx
                        newY = posY + dy

                        if newX < 0 or newX >= m or newY < 0 or newY >= n or visited[newX][newY] == 1 or forest[newX][
                            newY] == 0:
                            continue

                        visited[newX][newY] = 1
                        queue.append((newX, newY))

                step += 1
            return sys.maxint

        res = 0
        x = 0
        y = 0
        while len(trees) != 0:

            h, targetX, targetY = trees.pop()
            step = bfs(x, y, targetX, targetY)
            if step == sys.maxint:
                return -1
            res += step
            x = targetX
            y = targetY
            forest[x][y] = 1

        return res

