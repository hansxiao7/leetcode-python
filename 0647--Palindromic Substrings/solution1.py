class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp2 = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
            dp2[i][i] = 1
            if i != n - 1:
                if s[i] == s[i + 1]:
                    dp[i][i + 1] = 3
                    dp2[i][i + 1] = 1
                else:
                    dp[i][i + 1] = 2
                    dp2[i][i + 1] = 0

        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1] + dp2[i + 1][j - 1]
                    dp2[i][j] = dp2[i + 1][j - 1]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                    dp2[i][j] = 0

        return dp[0][n - 1]