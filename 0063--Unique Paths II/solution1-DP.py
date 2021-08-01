class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # DP
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        G = [[0 for _ in range(n)] for _ in range(m)]
        G[0][0] = 1

        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                break
            G[i][0] = 1

        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                break
            G[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    G[i][j] = 0
                    continue

                G[i][j] = G[i - 1][j] + G[i][j - 1]
        return G[m - 1][n - 1]
