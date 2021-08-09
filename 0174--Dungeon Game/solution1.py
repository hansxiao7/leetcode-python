class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[m - 1][n - 1] = 1
        if dungeon[m - 1][n - 1] <= 0:
            dp[m - 1][n - 1] = 1 - dungeon[m - 1][n - 1]
        else:
            dp[m - 1][n - 1] = 1

        for i in range(n - 2, -1, -1):
            dp[m - 1][i] = max(dp[m - 1][i + 1] - dungeon[m - 1][i], 1)

        for j in range(m - 2, -1, -1):
            dp[j][n - 1] = max(dp[j + 1][n - 1] - dungeon[j][n - 1], 1)

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(1, min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j])

        return dp[0][0]

