import heapq


class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        dp = [-sys.maxint for _ in range(len(nums))]
        dp[-1] = nums[-1]

        n = len(nums)
        heap = [(-nums[-1], n - 1)]

        n = len(nums)
        for i in range(n - 2, -1, -1):
            val, pos = heap[0]
            while pos < i + 1 or pos > min(i + k, n - 1):
                heapq.heappop(heap)
                val, pos = heap[0]
            dp[i] = nums[i] - val
            heapq.heappush(heap, (-dp[i], i))

        return dp[0]