class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        dp = [['' for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = s[i]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                temp = s[i:j + 1]
                dp[i][j] = temp
                for k in range(i, j):
                    left = dp[i][k]
                    right = dp[k + 1][j]

                    if len(left) + len(right) < len(dp[i][j]):
                        dp[i][j] = left + right

                # compress the string
                for k in range(i, j + 1):
                    pattern = s[i:k + 1]

                    if len(temp) % len(pattern) == 0 and temp.replace(pattern, '') == '':
                        compressed = str(len(temp) // len(pattern)) + '[' + dp[i][k] + ']'

                        if len(compressed) < len(dp[i][j]):
                            dp[i][j] = compressed

        return dp[0][n - 1]