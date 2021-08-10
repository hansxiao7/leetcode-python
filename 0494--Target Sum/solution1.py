class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 1:
            return int(abs(nums[0]) == abs(target))

        # DP
        n = len(nums)
        dp = [[0 for _ in range(10001)] for _ in range(n)]
        dp[0][nums[0] + 5000] += 1
        dp[0][-nums[0] + 5000] += 1

        for i in range(1, n):
            curr = nums[i]
            for total in range(-4000, 4001):
                j = total + 5000
                if dp[i - 1][j] != 0:
                    dp[i][j + curr] += dp[i - 1][j]
                    dp[i][j - curr] += dp[i - 1][j]

        return dp[n - 1][target + 5000]