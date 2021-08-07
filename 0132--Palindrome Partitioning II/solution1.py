class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        p_m = check_p(s)
        n = len(s)

        dp = [sys.maxint for _ in range(n)]
        dp[0] = 0

        for i in range(1, n):
            if p_m[0][i]:
                dp[i] = 0
                continue

            for j in range(i, -1, -1):
                if p_m[j][i]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[n - 1]


def check_p(s):
    n = len(s)

    dp = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = True
        if i < n - 1 and s[i + 1] == s[i]:
            dp[i][i + 1] = True

    for i in range(n - 3, -1, -1):
        for j in range(i + 2, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False

    return dp
