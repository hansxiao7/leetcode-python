class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        flip = 0
        nonflip = 0
        result = 0

        for i in range(n):

            if nums[i] == 0:
                flip = nonflip + 1
                nonflip = 0
            if nums[i] == 1:
                nonflip += 1
                flip += 1
            result = max(flip, nonflip, result)

        return result
