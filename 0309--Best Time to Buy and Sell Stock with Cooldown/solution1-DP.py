class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # DP
        G = [0 for _ in range(len(prices))]

        for i in range(len(prices) - 2, -1, -1):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    if j + 2 < len(prices):
                        G[i] = max(G[i], prices[j] - prices[i] + G[j + 2])
                    else:
                        G[i] = max(G[i], prices[j] - prices[i])

                else:
                    G[i] = max(G[i], G[j])

        return G[0]