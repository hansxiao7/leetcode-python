class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # DP
        counts = []
        for i in range(len(strs)):
            word = strs[i]
            count_0 = 0
            count_1 = 0

            for j in range(len(word)):
                if word[j] == '1':
                    count_1 += 1
                else:
                    count_0 += 1
            counts.append((count_0, count_1))

        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs) + 1)]

        for i in range(1, len(strs) + 1):
            word = strs[i - 1]
            count_0 = counts[i - 1][0]
            count_1 = counts[i - 1][1]
            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= count_0 and k >= count_1:
                        dp[i][j][k] = max(dp[i - 1][j - count_0][k - count_1] + 1, dp[i - 1][j][k])
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
        return dp[len(strs)][m][n]
