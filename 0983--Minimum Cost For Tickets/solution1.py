class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """

        cache = {}

        def dfs(pos, max_d):
            if cache.get((pos, max_d)):
                return cache[(pos, max_d)]
            if pos >= len(days):
                return 0
            result = sys.maxint
            if days[pos] > max_d:
                temp1 = costs[0] + dfs(pos + 1, days[pos])
                temp2 = costs[1] + dfs(pos + 1, days[pos] + 6)
                temp3 = costs[2] + dfs(pos + 1, days[pos] + 29)
                result = min(temp1, temp2, temp3)
            else:  # days[pos] <= max_d
                result = dfs(pos + 1, max_d)
            cache[(pos, max_d)] = result
            return result

        return dfs(0, 0)