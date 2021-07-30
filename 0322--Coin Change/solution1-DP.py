class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # DP
        G = [[sys.maxint for _ in range(amount + 1)] for _ in range(len(coins))]

        G[0][0] = 0

        for i in range(1, amount + 1):
            if i % coins[0] == 0:
                G[0][i] = i // coins[0]

        for i in range(1, len(coins)):
            curr_price = coins[i]
            G[i][0] = 0

            for j in range(1, amount + 1):
                if j >= curr_price:
                    G[i][j] = min(G[i][j], G[i - 1][j], G[i][j - curr_price] + 1)
                else:
                    G[i][j] = G[i - 1][j]
        if G[len(coins) - 1][amount] == sys.maxint:
            return -1
        return G[len(coins) - 1][amount]