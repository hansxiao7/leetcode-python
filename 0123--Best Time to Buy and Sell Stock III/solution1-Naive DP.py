class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        G = [[0 for _ in range(len(prices))] for _ in range(2)]

        for i in range(len(prices) - 2, -1, -1):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    G[0][i] = max(G[0][i], prices[j] - prices[i])
                    if j + 1 < len(prices):
                        G[1][i] = max(G[1][i], prices[j] - prices[i] + G[0][j + 1])

                G[0][i] = max(G[0][i], G[0][j])
                G[1][i] = max(G[1][i], G[1][j])

        return max(G[0][0], G[1][0])
