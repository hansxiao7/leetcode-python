class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        error = sys.maxint
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if abs(nums[left] + nums[right] + nums[i] - target) < error:
                    error = abs(nums[left] + nums[right] + nums[i] - target)
                    result = nums[left] + nums[right] + nums[i]
                if error == 0:
                    return target
                if nums[left] + nums[right] + nums[i] > target:
                    right -= 1
                else:
                    left += 1
        return result
