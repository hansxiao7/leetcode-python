class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        result = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                result = max(result, temp)
                temp = 0
            else:
                temp += 1
        result = max(temp, result)
        return result
