import heapq


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []

        temp = []

        for skyline in buildings:
            start = skyline[0]
            end = skyline[1]
            height = skyline[2]

            temp.append([start, -height])
            temp.append([end, height])

        temp.sort()

        prev = 0
        heap = [0]

        for i in range(len(temp)):
            pos = temp[i][0]
            h = temp[i][1]
            if h < 0:
                heapq.heappush(heap, h)
            else:
                heap.remove(-h)
                heapq.heapify(heap)

            curr_max = -heap[0]
            if curr_max != prev:
                result.append([pos, curr_max])
                prev = curr_max

        return result