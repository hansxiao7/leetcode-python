class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        def lcs(s1, s2):
            m = len(s1)
            n = len(s2)

            dp = [['' for _ in range(n + 1)] for _ in range(m + 1)]

            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if s1[i - 1] == s2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
                    else:
                        if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                            dp[i][j] = dp[i - 1][j]
                        else:
                            dp[i][j] = dp[i][j - 1]

            return dp[m][n]

        s = lcs(str1, str2)
        result = ''
        m = 0
        n = 0
        for i in range(len(s)):
            while str1[m] != s[i]:
                result = result + str1[m]
                m += 1
            m += 1

            while str2[n] != s[i]:
                result = result + str2[n]
                n += 1
            n += 1

            result = result + s[i]

        result = result + str1[m:] + str2[n:]
        return result