class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        add = [0 for _ in range(n + 1)]

        result = -sys.maxint
        for i in range(1, n + 1):
            add[i] = max(nums[i - 1], add[i - 1] + nums[i - 1])

            result = max(add[i], result)

        return result