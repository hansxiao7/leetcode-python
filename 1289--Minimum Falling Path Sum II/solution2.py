class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dp = [0] * n
        minPos = None
        secondMin = None
        for i in range(n):
            v = grid[-1][i]
            dp[i] = v
            if minPos is None or v < grid[-1][minPos]:
                secondMin = minPos
                minPos = i
            elif secondMin is None or v < grid[-1][secondMin]:
                secondMin = i

        prevMinPos = minPos
        prevSecondMin = secondMin
        for i in range(m - 2, -1, -1):
            minPos = None
            secondMin = None
            temp1 = dp[prevMinPos]
            temp2 = dp[prevSecondMin]
            for j in range(n):
                # update the dp
                if j != prevMinPos:
                    dp[j] = temp1 + grid[i][j]
                else:
                    dp[j] = temp2 + grid[i][j]

                # update the min and secondMin positions
                if minPos is None or dp[j] < dp[minPos]:
                    secondMin = minPos
                    minPos = j
                elif secondMin is None or dp[j] < dp[secondMin]:
                    secondMin = j

            prevMinPos = minPos
            prevSecondMin = secondMin

        return min(dp)


