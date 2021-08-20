class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = (1 << (len(nums) + 1)) - 1
        temp = 0
        for i in range(len(nums)):
            temp |= 1 << nums[i]

        temp2 = target & ~temp

        for i in range(len(nums) + 1):
            if temp2 == 1 << i:
                return i

