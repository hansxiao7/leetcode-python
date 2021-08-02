class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        m = len(costs)
        f = [[0 for _ in range(3)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            f[i][0] = min(f[i - 1][1], f[i - 1][2]) + costs[i - 1][0]
            f[i][1] = min(f[i - 1][0], f[i - 1][2]) + costs[i - 1][1]
            f[i][2] = min(f[i - 1][0], f[i - 1][1]) + costs[i - 1][2]

        return min(f[m])