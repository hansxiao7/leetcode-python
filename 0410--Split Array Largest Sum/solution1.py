class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        sum_m = calculate_sum(nums)

        dp = [[sys.maxint for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][1] = sum_m[0][i]

        for i in range(1, n + 1):
            for j in range(2, min(m + 1, i + 1)):
                for l in range(i - 1, j - 2, -1):
                    if max(sum_m[l][i], dp[l][j - 1]) > dp[i][j]:
                        break
                    dp[i][j] = min(dp[i][j], max(sum_m[l][i], dp[l][j - 1]))

        return dp[n][m]


def calculate_sum(nums):
    n = len(nums)

    sum_m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        sum_m[i - 1][i] = nums[i - 1]

    for i in range(n):
        for j in range(i + 2, n + 1):
            sum_m[i][j] = sum_m[i][j - 1] + nums[j - 1]

    return sum_m