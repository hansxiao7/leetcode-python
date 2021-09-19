class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[[0 for _ in range(m + 1)] for _ in range(n + 1)] for _ in range(m + 1)]  # dp[x1][y1][x2]

        for x1 in range(m, -1, -1):
            for y1 in range(n, -1, -1):
                for x2 in range(m, -1, -1):
                    y2 = x1 + y1 - x2
                    if x1 == x2 and y1 == y2 and x1 == m - 1 and y1 == n - 1:
                        dp[x1][y1][x2] = grid[m - 1][n - 1]
                        continue
                    if x1 >= m or x2 >= m or y1 >= n or y2 >= n:
                        dp[x1][y1][x2] = -sys.maxint
                        continue
                    if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                        dp[x1][y1][x2] = -sys.maxint
                        continue

                    if x1 == x2 and y1 == y2:
                        temp = grid[x1][y1]
                    else:
                        temp = grid[x1][y1] + grid[x2][y2]

                    dp[x1][y1][x2] = temp + max(dp[x1 + 1][y1][x2 + 1], dp[x1][y1 + 1][x2 + 1], dp[x1 + 1][y1][x2],
                                                dp[x1][y1 + 1][x2])

        res = dp[0][0][0]

        if res < 0:
            return 0
        return res