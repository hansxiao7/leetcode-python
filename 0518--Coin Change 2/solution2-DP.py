class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # DP
        n_coin = len(coins)
        G = [[0 for _ in range(amount + 1)] for _ in range(n_coin)]

        G[0][0] = 1
        for i in range(1, amount + 1):
            if i % coins[0] == 0:
                G[0][i] = 1

        for i in range(1, n_coin):
            curr_coin = coins[i]
            G[i][0] = 1
            for j in range(1, amount + 1):
                if j >= curr_coin:
                    G[i][j] = G[i][j - curr_coin] + G[i - 1][j]
                else:
                    G[i][j] = G[i - 1][j]

        return G[n_coin - 1][amount]
