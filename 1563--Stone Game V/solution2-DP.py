class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        prefix = [0]

        for s in stoneValue:
            prefix.append(prefix[-1] + s)

        n = len(stoneValue)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n - 1):
            dp[i][i + 1] = min(stoneValue[i], stoneValue[i + 1])
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                for k in range(i, j):
                    left = prefix[k + 1] - prefix[i]
                    right = prefix[j + 1] - prefix[k + 1]
                    if left > right:
                        dp[i][j] = max(dp[i][j], right + dp[k + 1][j])
                    elif right > left:
                        dp[i][j] = max(dp[i][j], left + dp[i][k])
                    else:
                        dp[i][j] = max(dp[i][j], left + dp[i][k], right + dp[k + 1][j])
        return dp[0][n - 1]