class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # BFS
        m = len(mat)
        n = len(mat[0])

        queue = []

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([i, j])

        visited = [[0 for _ in range(n)] for _ in range(m)]
        result = [[0 for _ in range(n)] for _ in range(m)]
        dis = 0

        while len(queue) != 0:
            n_q = len(queue)

            for i in range(n_q):
                x, y = queue.pop(0)
                visited[x][y] = 1

                result[x][y] = dis

                if x - 1 >= 0 and visited[x - 1][y] == 0 and mat[x - 1][y] != 0:
                    visited[x - 1][y] = 1
                    queue.append([x - 1, y])

                if x + 1 < m and visited[x + 1][y] == 0 and mat[x + 1][y] != 0:
                    visited[x + 1][y] = 1
                    queue.append([x + 1, y])

                if y - 1 >= 0 and visited[x][y - 1] == 0 and mat[x][y - 1] != 0:
                    visited[x][y - 1] = 1
                    queue.append([x, y - 1])

                if y + 1 < n and visited[x][y + 1] == 0 and mat[x][y + 1] != 0:
                    visited[x][y + 1] = 1
                    queue.append([x, y + 1])

            dis += 1

        return result
