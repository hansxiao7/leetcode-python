class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        l = 0
        count = 0
        result = 0
        for r in range(len(nums)):
            if nums[r] >= left and nums[r] <= right:
                count = r - l + 1
                result += r - l + 1
            elif nums[r] < left:
                result += count
            else:
                l = r + 1
                count = 0

        return result