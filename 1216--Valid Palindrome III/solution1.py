class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        t = s[::-1]

        m = len(s)

        dp = [[0 for _ in range(m + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        if m - dp[m][m] <= k:
            return True
        return False