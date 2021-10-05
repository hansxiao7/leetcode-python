class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0

        while i < len(nums) - 1 and nums[i + 1] - nums[i] == 0:
            i += 1

        if i == len(nums) - 1:
            return True

        temp = nums[i + 1] - nums[i]

        for j in range(i + 1, len(nums) - 1):
            if (nums[j + 1] - nums[j]) == 0:
                continue
            elif (nums[j + 1] - nums[j]) * temp > 0:
                continue
            else:
                return False

        return True

