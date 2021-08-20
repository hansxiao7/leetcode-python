class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        if nums[right] - nums[0] - right < k:
            return nums[0] + k + right

        while left < right:
            mid = (left + right) // 2
            l = nums[mid] - nums[0] - mid
            if l < k:
                left = mid + 1
            elif l >= k:
                right = mid

        return nums[0] + k + left - 1