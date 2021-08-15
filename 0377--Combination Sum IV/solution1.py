class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == target:
                return 1
            else:
                return 0
        cache = {}

        def helper(target):
            if target in cache:
                return cache[target]
            if target == 0:
                return 1
            elif target < 0:
                return 0

            result = 0
            for i in range(len(nums)):
                result += helper(target - nums[i])
            cache[target] = result
            return result

        return helper(target)