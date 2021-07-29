class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # DP
        m = len(mat)
        n = len(mat[0])

        dist = [[sys.maxint for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i < m - 1:
                        dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                    if j < n - 1:
                        dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)

        return dist