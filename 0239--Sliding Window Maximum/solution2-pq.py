import heapq


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []

        res = [None] * (len(nums) - k + 1)

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        res[0] = -heap[0][0]

        for i in range(k, len(nums)):
            while len(heap) != 0 and i - heap[0][1] >= k:
                heapq.heappop(heap)

            heapq.heappush(heap, (-nums[i], i))

            res[i - k + 1] = -heap[0][0]

        return res
