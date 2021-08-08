class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(1)
        nums.insert(0, 1)

        n = len(nums)

        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n - 2, 0, -1):
            for j in range(i, n - 1):
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] + dp[k + 1][j])
        return dp[1][n - 2]

