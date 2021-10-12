class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 10 ** n
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 10

        temp = 9
        for i in range(2, n + 1):
            temp = temp * (10 - i + 1)
            dp[i] = dp[i - 1] + temp

        return dp[n]


