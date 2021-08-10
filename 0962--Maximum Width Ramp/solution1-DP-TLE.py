class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0 for _ in range(n)]

        result = 0

        for i in range(1, n):
            for j in range(i):
                if nums[j] <= nums[i]:
                    dp[i] = max(dp[i], i - j + dp[j])
            result = max(result, dp[i])

        return result