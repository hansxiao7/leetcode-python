class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        dp = [0] * (n + 1)

        temp = 0
        for i in range(k, n + 1):
            dp[i] = 1

        for i in range(1, maxPts + 1):
            if k - 1 + i <= n:
                temp += 1. / maxPts

        for i in range(k - 1, -1, -1):
            dp[i] = temp
            temp += (1. / maxPts) * dp[i]
            if (i + maxPts) <= n:
                temp -= (1. / maxPts) * dp[i + maxPts]

        return dp[0]