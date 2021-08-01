class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # DP
        G = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            G[i][0] = 1
        for i in range(n):
            G[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                G[i][j] = G[i - 1][j] + G[i][j - 1]

        return G[m - 1][n - 1]