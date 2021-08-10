class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        m = len(group)
        maxP = minProfit

        dp = [[[0 for _ in range(maxP + 1)] for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0][0] = 1

        for i in range(1, m + 1):
            val = profit[i - 1]
            req = group[i - 1]
            for j in range(n + 1):
                for k in range(maxP + 1):
                    if j >= req:
                        dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - req][max(0, k - val)]
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        result = 0
        for i in range(minProfit, maxP + 1):
            for j in range(n + 1):
                result += dp[m][j][i]
        return result % (10 ** 9 + 7)

