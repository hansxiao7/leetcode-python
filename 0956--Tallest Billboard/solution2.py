class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        maxH = sum(rods)

        n = len(rods)
        dp = [[-1 for _ in range(2 * maxH + 1)] for _ in range(n + 1)]
        dp[0][maxH] = 0

        result = 0
        for i in range(1, n + 1):
            h = rods[i - 1]
            for d in range(-maxH, maxH + 1):
                j = d + maxH
                if j + h <= 2 * maxH:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j + h])
                if j - h >= 0 and dp[i - 1][j - h] != -1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - h] + h)

        return dp[n][maxH]