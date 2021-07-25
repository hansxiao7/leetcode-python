class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 1. brute force, time limit exceeded
        # 2. remember past min
        result = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                result = max(result, prices[i] - min_price)

        return result