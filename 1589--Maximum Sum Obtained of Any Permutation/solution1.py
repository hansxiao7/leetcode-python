class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        times = [0 for _ in range(n)]

        for r in requests:
            times[r[0]] += 1
            if r[1] + 1 < len(nums):
                times[r[1] + 1] -= 1
        for i in range(1, n):
            times[i] += times[i - 1]

        times.sort()
        nums.sort()
        result = 0
        for i in range(n):
            result += times[i] * nums[i]

        return result % (10 ** 9 + 7)