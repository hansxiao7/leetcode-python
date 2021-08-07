class Solution(object):
    def largestSumOfAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)

        dp = [[-sys.maxint for _ in range(k + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][1] = sum(nums[:i]) / float(i)

        for i in range(1, n + 1):
            for j in range(2, k + 1):
                for m in range(i - 1, 0, -1):
                    dp[i][j] = max(dp[m][j - 1] + sum(nums[m:i]) / float(i - m), dp[i][j])

        return dp[n][k]