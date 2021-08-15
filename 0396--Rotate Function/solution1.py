class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)

        temp = [0 for _ in range(len(nums))]

        for i in range(len(nums)):
            temp[i] = total - nums[i]

        dp = [0 for _ in range(len(nums))]

        n = len(nums)
        temp2 = 0
        for i in range(n):
            dp[0] += temp2 * nums[i]
            temp2 += 1

        result = dp[0]
        for i in range(1, n):
            dp[i] = dp[i - 1] - (n - 1) * nums[n - i] + temp[n - i]
            result = max(result, dp[i])

        return result
