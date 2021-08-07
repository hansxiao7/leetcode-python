class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # dp
        n = len(s)
        dp = [[False for _ in range(4)] for _ in range(n)]
        p_m = check_p(s)

        for i in range(n):
            dp[i][1] = p_m[0][i]

        for i in range(n):
            for k in range(2, 4):
                for j in range(i):
                    if p_m[j + 1][i]:
                        dp[i][k] = dp[i][k] or dp[j][k - 1]

        return dp[n - 1][3]


def check_p(s):
    n = len(s)

    dp = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                if j == i + 1:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False

    return dp