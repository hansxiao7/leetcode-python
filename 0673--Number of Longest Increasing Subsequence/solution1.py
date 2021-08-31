class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[1, 1] for _ in range(len(nums))]
        maxLength = 1
        for i in range(len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]

            maxLength = max(maxLength, dp[i][0])

        result = 0
        for i in range(len(dp)):
            if dp[i][0] == maxLength:
                result += dp[i][1]

        return result
