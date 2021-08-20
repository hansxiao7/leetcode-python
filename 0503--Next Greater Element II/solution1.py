class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = nums + nums
        result = [-1 for _ in range(len(nums))]
        stack = []

        for i in range(len(nums) - 1, -1, -1):
            while len(stack) != 0 and nums[i] >= stack[-1]:
                stack.pop()

            if len(stack) != 0:
                result[i] = stack[-1]

            stack.append(nums[i])

        return result[:len(nums) // 2]