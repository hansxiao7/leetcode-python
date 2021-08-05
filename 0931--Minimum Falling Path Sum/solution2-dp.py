class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        dp = [[sys.maxint for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[n - 1][i] = matrix[n - 1][i]

        for i in range(n - 2, -1, -1):
            for j in range(n):
                left = max(0, j - 1)
                mid = j
                right = min(n - 1, j + 1)
                dp[i][j] = matrix[i][j] + min(dp[i + 1][left], dp[i + 1][mid], dp[i + 1][right])
        return min(dp[0])