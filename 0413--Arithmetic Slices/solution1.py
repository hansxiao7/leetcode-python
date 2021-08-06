class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n < 3:
            return 0

        dp = [0 for _ in range(n + 1)]

        for i in range(3, n + 1):
            if nums[i - 1] - nums[i - 2] == nums[i - 2] - nums[i - 3]:
                dp[i] = dp[i - 1] + 1

        return sum(dp)