class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        cost_m = cost(s)
        dp = [[sys.maxint for _ in range(k + 1)] for _ in range(n)]

        for i in range(n):
            dp[i][1] = cost_m[0][i]

        for i in range(n):
            for j in range(2, k + 1):
                for m in range(i):
                    dp[i][j] = min(dp[i][j], dp[m][j - 1] + cost_m[m + 1][i])
        return dp[n - 1][k]


def cost(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + dp[i + 1][j - 1]

    return dp