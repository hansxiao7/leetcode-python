class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0

        for i in range(len(nums) - 2):
            if nums[i] == 0:
                continue
            temp = nums[i]
            right = i + 2
            for left in range(i + 1, len(nums)):
                while right < len(nums) and nums[right] < nums[left] + temp:
                    right += 1
                result += right - left - 1

        return result
