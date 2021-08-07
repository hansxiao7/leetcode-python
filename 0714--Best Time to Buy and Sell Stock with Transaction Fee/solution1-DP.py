class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        hold = [0 for _ in range(n)]
        cash = [0 for _ in range(n)]

        hold[0] = -prices[0]

        for i in range(1, n):
            cash[i] = max(cash[i - 1], hold[i - 1] - fee + prices[i])
            hold[i] = max(hold[i - 1], cash[i] - prices[i])

        return max(hold[n - 1], cash[n - 1])