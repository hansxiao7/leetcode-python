import heapq


class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        heap = sticks
        heapq.heapify(sticks)
        result = 0

        while len(sticks) >= 2:
            temp = 0
            for i in range(2):
                temp += heapq.heappop(heap)

            heapq.heappush(heap, temp)
            result += temp

        return result