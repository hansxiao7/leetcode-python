class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return False

        dp = [False for _ in range(n + 1)]

        dp[1] = False
        dp[2] = True

        for i in range(3, n + 1):
            for j in range(1, i):
                if i % j == 0:
                    dp[i] = dp[i] or dp[j]

        return dp[n]

