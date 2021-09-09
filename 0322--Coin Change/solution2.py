class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        m = len(coins)

        dp = [sys.maxint for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, m + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[j] = min(1 + dp[j - coins[i - 1]], dp[j])

        res = dp[amount]
        if res == sys.maxint:
            return -1
        return res