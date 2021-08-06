class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [sys.maxint for i in range(n + 1)]
        dp[1] = 1

        count = 2
        squares = [1]

        for i in range(2, n + 1):
            if i == count ** 2:
                squares.append(i)
                dp[i] = 1
                count += 1
                continue

            for j in range(len(squares)):
                dp[i] = min(dp[i], 1 + dp[i - squares[j]])

        return dp[n]

