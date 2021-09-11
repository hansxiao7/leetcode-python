class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)

        dp1[1] = nums[0]
        dp2[1] = nums[1]

        for i in range(2, len(nums)):
            dp1[i] = max(dp1[i - 2] + nums[i - 1], dp1[i - 1])
            dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])

        return max(dp1[len(nums) - 1], dp2[len(nums) - 1])
