class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1

        for num in nums:
            if nums[abs(num)] > 0:
                nums[abs(num)] *= -1
            else:
                return abs(num)
