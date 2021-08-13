class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            x = len(nums) - i

            if nums[i] >= x:
                if i == 0:
                    return x
                elif nums[i - 1] < x:
                    return x
        return -1