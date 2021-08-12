class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0

        left = 0
        temp = 1

        for right in range(len(nums)):
            temp = temp * nums[right]

            while temp >= k and left <= right:
                temp = temp / nums[left]
                left += 1

            result += right - left + 1

        return result