class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        prefix = [0 for _ in range(n + 1)]

        total = 0
        result = -sys.maxint
        for i in range(len(nums)):
            total += nums[i]
            prefix[i + 1] = total

            if i + 1 - k >= 0:
                for j in range(i + 1 - k, -1, -1):
                    temp = (total - prefix[j]) / (i + 1.0 - j)
                    result = max(result, temp)

        return result