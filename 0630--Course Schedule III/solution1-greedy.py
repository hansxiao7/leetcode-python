class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key=lambda x: x[1])

        import heapq

        heap = []

        n = 0

        for i in range(len(courses)):
            dur = courses[i][0]
            end = courses[i][1]

            if n + dur <= end:
                heapq.heappush(heap, -dur)
                n += dur

            else:
                if len(heap) != 0 and -heap[0] > dur:
                    prev = heapq.heappop(heap)
                    heapq.heappush(heap, -dur)
                    n = n + dur + prev

        return len(heap)