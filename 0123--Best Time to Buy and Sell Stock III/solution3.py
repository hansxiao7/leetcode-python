class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = len(prices)

        dp = [[-sys.maxint for _ in range(5)] for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 0

        for i in range(1, m + 1):
            for j in range(1, 5):
                if j % 2 != 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i - 1])

        res = max(dp[m])
        return res