class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total = sum(stones)
        target = total / 2

        m = len(stones)
        dp = [0 for _ in range(target + 1)]

        for i in range(1, m + 1):
            for j in range(target, -1, -1):
                if j >= stones[i - 1]:
                    dp[j] = max(dp[j - stones[i - 1]] + stones[i - 1], dp[j])

        return total - 2 * dp[target]