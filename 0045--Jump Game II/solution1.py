class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [sys.maxint for _ in range(n)]
        dp[n - 1] = 0
        for i in range(n - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j >= n:
                    break
                dp[i] = min(dp[i + j] + 1, dp[i])

        return dp[0]
