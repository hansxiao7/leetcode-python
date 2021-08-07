class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        cash = [0 for _ in range(n)]
        hold = [0 for _ in range(n)]

        hold[0] = -prices[0]

        for i in range(1, n):
            cash[i] = max(cash[i - 1], hold[i - 1] + prices[i])
            hold[i] = max(cash[i] - prices[i], hold[i - 1])

        return cash[n - 1]