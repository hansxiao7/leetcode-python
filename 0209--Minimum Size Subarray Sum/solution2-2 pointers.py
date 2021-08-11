class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        result = sys.maxint
        left = 0

        for i in range(len(nums)):
            total += nums[i]

            while total >= target:
                result = min(result, i - left + 1)
                total -= nums[left]
                left += 1

        if result == sys.maxint:
            return 0
        return result