class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total = sum(stones)
        target = total / 2

        m = len(stones)
        dp = [[0 for _ in range(target + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, target + 1):
                if j >= stones[i - 1]:
                    dp[i][j] = max(dp[i - 1][j - stones[i - 1]] + stones[i - 1], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        return total - 2 * dp[m][target]