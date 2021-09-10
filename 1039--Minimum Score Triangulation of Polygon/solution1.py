class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        m = len(values)

        dp = [[sys.maxint for _ in range(m)] for _ in range(m)]

        for i in range(m):
            dp[i][i] = 0

            if i < m - 1:
                dp[i][i + 1] = 0

        for i in range(m - 1, -1, -1):
            for j in range(i + 2, m):
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[k] * values[j])

        return dp[0][m - 1]