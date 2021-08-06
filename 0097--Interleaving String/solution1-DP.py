class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        m = len(s1)
        n = len(s2)

        if len(s3) != m + n:
            return False

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]
                else:
                    dp[i][j] = (s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]) or (
                                s1[i - 1] == s3[i + j - 1] and dp[i - 1][j])
        return dp[m][n]
