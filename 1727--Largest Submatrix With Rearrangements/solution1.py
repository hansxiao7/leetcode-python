class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            if matrix[0][j] == 1:
                dp[0][j] = 1

        for j in range(n):
            for i in range(1, m):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + dp[i - 1][j]

        res = 0
        for i in range(m):
            dp[i].sort(key=lambda x: -x)
            for j in range(n):
                if dp[i][j] == 0:
                    break
                res = max(res, (j + 1) * dp[i][j])

        return res