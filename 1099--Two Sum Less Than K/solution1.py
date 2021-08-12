class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        left = 0
        right = len(nums) - 1
        diff = sys.maxint
        result = None

        while left < right:
            temp = nums[left] + nums[right]
            if temp < k:
                curr_diff = k - temp
                if curr_diff < diff:
                    diff = curr_diff
                    result = temp
                left += 1
            elif temp >= k:
                right -= 1

        if result is None:
            return -1
        return result