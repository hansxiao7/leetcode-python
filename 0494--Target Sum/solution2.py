class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = sum(nums)
        if len(nums) == 1:
            if abs(nums[0]) == abs(target):
                return 1
            else:
                return 0
        t = (total + target) / 2
        if (total + target) % 2 != 0:
            return 0

        m = len(nums)
        dp = [[0 for _ in range(t + 1)] for _ in range(m + 1)]
        dp[0][0] = 1

        for i in range(1, m + 1):
            dp[i][0] = 1
            for j in range(t + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][t]