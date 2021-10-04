class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []

        s3 = -sys.maxint

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < s3:
                return True

            while len(stack) != 0 and nums[i] > stack[-1]:
                s3 = max(s3, stack.pop())

            stack.append(nums[i])

        return False