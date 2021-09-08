class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
                    elif p[j - 1] == '*':
                        dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                    else:
                        dp[i][j] = False
        return dp[m][n]
