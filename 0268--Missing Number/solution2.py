class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        for num in nums:
            res = res ^ num
        n = len(nums)
        for i in range(n + 1):
            res = res ^ i

        return res