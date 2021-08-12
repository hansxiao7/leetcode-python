class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        temp = nums[i]

        while i < j:
            while i < j and nums[j] % 2 != 0:
                j -= 1
            nums[i] = nums[j]

            while i < j and nums[i] % 2 == 0:
                i += 1
            nums[j] = nums[i]

        nums[i] = temp
        return nums
