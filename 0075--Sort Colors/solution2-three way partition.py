class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # three-way partition
        i = 0
        j = 0
        k = len(nums) - 1

        target = 1

        while j <= k:
            if nums[j] < target:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
            elif nums[j] > target:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1

