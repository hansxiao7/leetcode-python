class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if len(nums) < 2:
            return False

        if total % 2 == 1:
            return False

        target = total / 2

        n = len(nums)
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

        if nums[0] <= target:
            dp[1][nums[0]] = True

        for i in range(2, n + 1):
            num = nums[i - 1]
            for j in range(target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]