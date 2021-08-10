import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = []
        for i in range(len(stones)):
            heapq.heappush(heap, -stones[i])

        while len(heap) > 1:
            temp = []
            for i in range(2):
                temp.append(heapq.heappop(heap))

            result = abs(temp[0] - temp[1])

            if result == 0:
                continue
            else:
                heapq.heappush(heap, -result)
        if len(heap) == 0:
            return 0
        return -heap[0]
