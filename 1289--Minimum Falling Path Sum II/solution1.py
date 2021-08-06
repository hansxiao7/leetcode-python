class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """

        # iterate the last row
        min_id = None
        second_min = None

        m = len(arr)
        n = len(arr[0])

        dp = [[sys.maxint for _ in range(n)] for _ in range(m)]

        for i in range(n):
            dp[m - 1][i] = arr[m - 1][i]
            if min_id is None or dp[m - 1][i] < dp[m - 1][min_id]:
                second_min = min_id
                min_id = i
            elif second_min is None or dp[m - 1][i] < dp[m - 1][second_min]:
                second_min = i

        prev_min = min_id
        prev_second_min = second_min

        for i in range(m - 2, -1, -1):
            min_id = None
            second_min = None
            for j in range(n):
                if j == prev_min:
                    dp[i][j] = arr[i][j] + dp[i + 1][prev_second_min]
                else:
                    dp[i][j] = arr[i][j] + dp[i + 1][prev_min]

                if min_id is None or dp[i][j] < dp[i][min_id]:
                    second_min = min_id
                    min_id = j
                elif second_min is None or dp[i][j] < dp[i][second_min]:
                    second_min = j

            prev_min = min_id
            prev_second_min = second_min

        return dp[0][min_id]