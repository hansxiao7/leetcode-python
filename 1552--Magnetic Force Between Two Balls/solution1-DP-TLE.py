class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        m = m - 1
        # dp
        n = len(position)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        temp = 0
        for i in range(1, n + 1):
            dp[i][1] = position[i - 1] - position[0]

        for i in range(1, n + 1):
            for k in range(2, min(m + 1, i + 1)):
                for j in range(i - 1, k - 2, -1):
                    dp[i][k] = max(dp[i][k], min(dp[j][k - 1], position[i - 1] - position[j - 1]))

        return dp[n][m]