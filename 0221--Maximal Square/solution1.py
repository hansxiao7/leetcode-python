class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        result = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    result = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1' and matrix[i - 1][j] == '1' and matrix[i][j - 1] == '1' and matrix[i - 1][
                    j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

                result = max(result, dp[i][j])

        return result ** 2