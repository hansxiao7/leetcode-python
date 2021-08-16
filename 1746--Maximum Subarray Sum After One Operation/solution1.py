class Solution(object):
    def maxSumAfterOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        changed = [0 for _ in range(n)]
        unchanged = [0 for _ in range(n)]

        changed[0] = nums[0] ** 2
        unchanged[0] = nums[0]

        result = max(changed[0], unchanged[0])
        for i in range(1, n):
            changed[i] = max(nums[i] ** 2, unchanged[i - 1] + nums[i] ** 2, changed[i - 1] + nums[i])
            unchanged[i] = max(nums[i], unchanged[i - 1] + nums[i])

            result = max(result, changed[i], unchanged[i])

        return result