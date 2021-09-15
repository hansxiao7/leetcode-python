class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0 for _ in range(n)]

        for i in range(n):
            if obstacleGrid[0][i] == 0:
                dp[i] = 1
            else:
                break

        for i in range(1, m):
            if obstacleGrid[i][0] != 0:
                dp[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[j] = dp[j] + dp[j - 1]
                else:
                    dp[j] = 0

        return dp[n - 1]