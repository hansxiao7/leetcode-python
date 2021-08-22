class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        n = len(nums)

        dp = [{} for _ in range(n)]
        dp[0] = {0: 1}

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = max(dp[i].get(diff, 1), 1 + dp[j].get(diff, 1))

                result = max(result, dp[i][diff])
        return result