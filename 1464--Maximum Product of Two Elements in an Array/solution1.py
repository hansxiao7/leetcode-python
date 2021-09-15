class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxValue = -1
        res = 0
        for i in range(len(nums)):
            res = max(res, (nums[i] - 1) * maxValue)
            maxValue = max(maxValue, nums[i] - 1)

        return res
