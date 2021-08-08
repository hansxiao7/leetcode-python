class Solution(object):
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)

        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i < n - 1:
                if arr[i] == arr[i + 1]:
                    dp[i][i + 1] = 1
                else:
                    dp[i][i + 1] = 2

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                temp = sys.maxint
                if arr[i] == arr[j]:
                    temp = min(temp, dp[i + 1][j - 1])
                for k in range(i, j):
                    temp = min(temp, dp[i][k] + dp[k + 1][j])
                dp[i][j] = temp

        return dp[0][n - 1]