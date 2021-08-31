class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = -sys.maxint
        result = 0
        curr = 0

        for i in range(len(nums)):
            if nums[i] > prev:
                curr += 1
            else:
                result = max(result, curr)
                curr = 1

            prev = nums[i]

        return max(curr, result)