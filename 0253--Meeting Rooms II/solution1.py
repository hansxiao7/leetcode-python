import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[0])

        heap = []

        for i in range(len(intervals)):
            startT, endT = intervals[i]
            if len(heap) == 0 or startT < heap[0]:
                heapq.heappush(heap, endT)
            elif startT >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, endT)

        return len(heap)