class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2 or k == 0:
            return 0

        li = []
        curr_k = 0
        total_p = 0

        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                total_p += prices[i + 1] - prices[i]
                curr_k += 1
                if len(li) != 0:
                    if i == li[-1][1]:
                        curr_k -= 1
                        li[-1] = [li[-1][0], i + 1]
                        continue
                li.append([i, i + 1])

        if k >= curr_k:
            return total_p
        else:
            while k < curr_k:
                condition = 0
                merge_loc = 0
                min_d = sys.maxint

                for j in range(len(li) - 1):
                    a = prices[li[j][1]] - prices[li[j][0]]
                    b = prices[li[j + 1][1]] - prices[li[j + 1][0]]
                    c = prices[li[j + 1][1]] - prices[li[j][0]]
                    diff = a + b - max(a, b, c)

                    if diff < min_d:
                        merge_loc = j
                        min_d = diff
                        if max(a, b, c) == a:
                            condition = 0
                        elif max(a, b, c) == b:
                            condition = 1
                        else:
                            condition = 2

                if condition == 0:
                    li.pop(merge_loc + 1)
                elif condition == 1:
                    li.pop(merge_loc)
                else:
                    li[merge_loc] = [li[merge_loc][0], li[merge_loc + 1][1]]
                    li.pop(merge_loc + 1)

                total_p -= min_d
                curr_k -= 1

        return total_p


