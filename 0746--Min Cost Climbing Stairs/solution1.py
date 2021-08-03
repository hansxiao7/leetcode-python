class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f = [0 for _ in range(len(cost) + 1)]

        f[0] = 0
        f[1] = 0

        n = len(cost)

        for i in range(2, n + 1):
            f[i] = min(f[i - 1] + cost[i - 1], f[i - 2] + cost[i - 2])

        return f[n]