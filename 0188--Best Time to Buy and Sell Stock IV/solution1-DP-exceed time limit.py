class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        G = [[0 for _ in range(k + 1)] for _ in range(len(prices))]

        for i in range(len(prices) - 2, -1, -1):  # start of sequence
            for j in range(i + 1, len(prices)):  # end of sequence
                for m in range(1, k + 1):  # number of operations
                    if j + 1 < len(prices):
                        G[i][m] = max(G[j][m], prices[j] - prices[i] + G[j][m - 1], G[i][m])
                    else:
                        if m == 1:
                            G[i][m] = max(G[j][m], G[i][m], prices[j] - prices[i])
                        else:
                            G[i][m] = max(G[j][m], G[i][m])
                    G[i][m] = max(G[i][m], G[i][m - 1])

        return G[0][k]