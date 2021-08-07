class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        m = len(jobDifficulty)

        dp = [[sys.maxint for _ in range(d + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][1] = max(jobDifficulty[:i])

        for i in range(1, m + 1):
            for j in range(2, d + 1):
                for k in range(i - 1, 0, -1):
                    dp[i][j] = min(dp[i][j], max(jobDifficulty[k:i]) + dp[k][j - 1])
        result = dp[m][d]

        if result == sys.maxint:
            return -1
        return result
