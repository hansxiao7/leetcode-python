class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        nums.sort()
        result = 0

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                temp = nums[i] + nums[left] + nums[right]

                if temp < target:
                    result += right - left
                    left += 1
                elif temp >= target:
                    right -= 1

        return result
