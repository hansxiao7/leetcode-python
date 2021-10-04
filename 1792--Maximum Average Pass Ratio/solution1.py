import heapq


class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        heap = []

        for x, y in classes:
            heapq.heappush(heap, (- (1 - x / float(y)) / (y + 1.), x, y))

        val = extraStudents

        while val > 0:
            _, x, y = heapq.heappop(heap)

            heapq.heappush(heap, (- (1 - (x + 1) / float(y + 1)) / (y + 2.), x + 1, y + 1))
            val -= 1

        res = 0

        for val, x, y in heap:
            res += x / float(y)

        return res / float(len(classes))