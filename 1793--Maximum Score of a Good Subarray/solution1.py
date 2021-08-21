class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        stack = []
        nums = [0] + nums + [0]
        result = 0

        for i in range(len(nums)):
            while len(stack) != 0 and nums[i] < nums[stack[-1]]:
                h = nums[stack.pop()]
                w = i - 1 - stack[-1]
                if i - 1 >= k + 1 and stack[-1] < k + 1:
                    result = max(result, w * h)

            stack.append(i)

        return result