class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        max_v = [0 for _ in range(n)]
        min_v = [0 for _ in range(n)]

        max_v[0] = nums[0]
        min_v[0] = nums[0]

        result = max_v[0]

        for i in range(1, n):
            max_v[i] = max(min_v[i - 1] * nums[i], max_v[i - 1] * nums[i], nums[i])
            min_v[i] = min(min_v[i - 1] * nums[i], max_v[i - 1] * nums[i], nums[i])

            result = max(result, max_v[i])

        return result