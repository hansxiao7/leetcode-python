class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1

        result = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[i // 2] + dp[i // 2 + 1]
            result = max(result, dp[i])

        return result