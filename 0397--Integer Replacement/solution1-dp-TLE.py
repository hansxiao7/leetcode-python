class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0] * (n + 1)

        dp[2] = 1
        dp[3] = 2

        for i in range(4, n + 1):
            if i % 2 == 0:
                dp[i] = 1 + dp[i // 2]
            else:
                dp[i] = min(1 + dp[i - 1], 2 + dp[(i + 1) // 2])

        return dp[n]
