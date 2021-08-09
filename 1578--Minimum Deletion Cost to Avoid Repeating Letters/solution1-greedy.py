class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        start = 0
        result = 0
        while start < len(s) - 1:
            if s[start] == s[start + 1]:
                temp_sum = cost[start]
                temp_max = cost[start]
                start = start + 1

                while start < len(s) and s[start] == s[start - 1]:
                    temp_sum += cost[start]
                    temp_max = max(temp_max, cost[start])
                    start += 1

                result += temp_sum - temp_max
            else:
                start += 1

        return result