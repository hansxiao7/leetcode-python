class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [1 for _ in range(n + 1)]
        right = [1 for _ in range(n + 1)]

        for i in range(1, n + 1):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 1, -1, -1):
            right[i] = right[i + 1] * nums[i]

        res = []
        for i in range(n):
            res.append(left[i] * right[i + 1])

        return res