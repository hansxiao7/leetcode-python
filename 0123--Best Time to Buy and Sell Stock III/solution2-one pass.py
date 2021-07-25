class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p_left = [0 for _ in range(len(prices))]
        p_right = [0 for _ in range(len(prices))]

        min_left = prices[0]
        max_right = prices[-1]

        for i in range(1, len(prices)):
            min_left = min(min_left, prices[i])
            p_left[i] = max(prices[i] - min_left, p_left[i - 1])

            max_right = max(max_right, prices[len(prices) - 1 - i])
            p_right[len(prices) - i - 1] = max(p_right[len(prices) - i], max_right - prices[len(prices) - i - 1])

        result = max(p_left)

        for j in range(len(prices) - 1):
            result = max(result, p_left[j] + p_right[j + 1])

        return result
