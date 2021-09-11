class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 2

        digits = [0] * 33
        for i in range(1, 33):
            digits[i] = n % 2
            n = n // 2

        dp = [0] * len(digits)
        dp[0] = 1
        dp[1] = 2

        for i in range(2, len(digits)):
            dp[i] = dp[i - 1] + dp[i - 2]

        res = 0
        i = 32
        while i >= 1:
            if digits[i] == 0:
                i -= 1
            else:
                res += dp[i - 1]
                if i >= 2 and digits[i - 1] == 1:
                    res += dp[i - 2]
                    return res
                else:
                    i -= 2
        res += 1
        return res
