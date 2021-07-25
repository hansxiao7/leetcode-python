class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        hold = [0 for _ in range(len(prices) + 1)]
        rest = [0 for _ in range(len(prices) + 1)]
        sold = [0 for _ in range(len(prices) + 1)]

        hold[0] = -sys.maxint

        for i in range(1, len(prices) + 1):
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i - 1])
            rest[i] = max(rest[i - 1], sold[i - 1])
            sold[i] = hold[i - 1] + prices[i - 1]
        print(hold)
        print(rest)
        print(sold)
        return max(sold[-1], rest[-1], 0)