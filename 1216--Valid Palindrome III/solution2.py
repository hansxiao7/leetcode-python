class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # lps
        m = len(s)

        dp = [[1 for _ in range(m)] for _ in range(m)]

        for i in range(m - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2

        for i in range(m - 3, -1, -1):
            for j in range(i + 2, m):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        if m - dp[0][m - 1] > k:
            return False
        return True