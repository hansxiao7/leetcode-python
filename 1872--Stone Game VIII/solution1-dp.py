class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        prefix = [0]
        for s in stones:
            prefix.append(prefix[-1] + s)

        n = len(stones)
        dp = [0] * len(stones)
        dp[-1] = best = prefix[-1]

        for i in range(n - 2, 0, -1):
            dp[i] = max(dp[i + 1], prefix[i + 1] - dp[i + 1])
        return dp[1]

