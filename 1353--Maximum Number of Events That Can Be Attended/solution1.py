import heapq


class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        if len(events) == 1:
            return 1

        end_d = -1
        for event in events:
            end_d = max(end_d, event[1])

        result = 0

        pos = 0
        events.sort()

        heap = []

        for start in range(1, end_d + 1):
            while pos < len(events) and events[pos][0] <= start:
                heapq.heappush(heap, events[pos][1])
                pos += 1

            while len(heap) != 0 and heap[0] < start:
                heapq.heappop(heap)

            if len(heap) != 0:
                heapq.heappop(heap)
                result += 1

        return result