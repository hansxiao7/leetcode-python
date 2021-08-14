class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        result = 1

        temp = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                temp += 1
            elif nums[i + 1] - nums[i] == 0:
                continue
            else:
                result = max(result, temp)
                temp = 1
        result = max(result, temp)
        return result