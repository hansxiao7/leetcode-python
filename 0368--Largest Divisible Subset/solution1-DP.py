class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        dp = [[] for _ in range(n)]

        for i in range(n):
            dp[i].append(nums[i])

        max_l = 1
        result = dp[0]
        for i in range(1, n):
            child = []
            temp = 1
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if len(dp[i]) + len(dp[j]) > temp:
                        child = dp[j]
                        temp = len(dp[i]) + len(dp[j])

            dp[i].extend(child)

            if len(dp[i]) > max_l:
                max_l = len(dp[i])
                result = dp[i]
        return result