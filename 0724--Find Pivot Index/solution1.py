class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = [0 for _ in range(n + 1)]
        right = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            left[i] = left[i - 1] + nums[i - 1]

        for i in range(n - 1, -1, -1):
            right[i] = right[i + 1] + nums[i]

        for i in range(n):
            if left[i] == right[i + 1]:
                return i
        return -1