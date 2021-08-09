class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """

        dp = [[[sys.maxint for _ in range(target + 1)] for _ in range(n)] for _ in range(m + 1)]
        dp[0][0][1] = 0

        for i in range(m):
            if houses[i] != 0:
                for j in range(n):
                    if j != houses[i] - 1:
                        cost[i][j] = sys.maxint
                    else:
                        cost[i][j] = 0
        temp = 0
        for j in range(n):
            temp = 0
            for i in range(1, m + 1):
                temp += cost[i - 1][j]
                dp[i][j][1] = temp

        for i in range(2, m + 1):
            for j in range(n):
                for k in range(2, target + 1):
                    for l in range(i - 1, -1, -1):

                        temp_sum = 0
                        for h in range(l, i):
                            temp_sum += cost[h][j]

                        temp1 = sys.maxint
                        for c in range(n):
                            if c != j:
                                temp1 = min(temp1, dp[l][c][k - 1])

                        dp[i][j][k] = min(dp[i][j][k], temp1 + temp_sum)

        result = sys.maxint

        for i in range(n):
            result = min(result, dp[m][i][target])

        if result == sys.maxint:
            return -1
        return result

