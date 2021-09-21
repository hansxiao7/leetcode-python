import heapq


class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        temp = []
        for start, end in intervals:
            temp.append((end - start + 1, start, end))

        temp.sort(key=lambda x: (x[1], x[0]))

        q_li = []

        for i in range(len(queries)):
            q_li.append((queries[i], i))

        q_li.sort()
        result = [-1] * len(queries)

        pos = 0
        heap = []
        for i in range(len(q_li)):
            index = q_li[i][1]
            num = q_li[i][0]

            while pos < len(temp) and temp[pos][1] <= num:
                heapq.heappush(heap, temp[pos])
                pos += 1

            while len(heap) != 0 and heap[0][2] < num:
                heapq.heappop(heap)

            if len(heap) != 0:
                result[index] = heap[0][0]

        return result