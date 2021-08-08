import heapq


class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        heap = []

        for i in range(len(piles)):
            heapq.heappush(heap, -piles[i])

        for i in range(k):
            val = heapq.heappop(heap)
            heapq.heappush(heap, val - (val + 1) // 2)

        return -sum(heap)
