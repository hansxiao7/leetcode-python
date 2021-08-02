class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        k = len(costs[0])

        if n == 1:
            return min(costs[0])

        f = [[0 for _ in range(k)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(k):
                min_val = sys.maxint
                for m in range(k):
                    if m != j and f[i - 1][m] < min_val:
                        min_val = f[i - 1][m]

                f[i][j] = min_val + costs[i - 1][j]

        return min(f[n])