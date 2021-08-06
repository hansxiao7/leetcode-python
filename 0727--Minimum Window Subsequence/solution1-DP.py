class Solution(object):
    def minWindow(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: str
        """
        m = len(s1)
        n = len(s2)

        dp = [[['', False] for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0][1] = True
        for i in range(m + 1):
            dp[i][0][1] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j][0] = dp[i - 1][j - 1][0] + s1[i - 1]
                    dp[i][j][1] = dp[i - 1][j - 1][1]
                else:
                    dp[i][j][0] = dp[i - 1][j][0] + s1[i - 1]
                    dp[i][j][1] = dp[i - 1][j][1]
        length = sys.maxint
        temp = ''
        for i in range(1, m + 1):
            if dp[i][n][1] == True:
                if len(dp[i][n][0]) < length:
                    length = len(dp[i][n][0])
                    temp = dp[i][n][0]
        return temp