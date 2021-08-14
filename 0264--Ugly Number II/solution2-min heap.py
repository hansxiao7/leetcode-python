import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        curr = 1
        heap = [1]
        visited = set()

        while True:
            temp = heapq.heappop(heap)

            if temp in visited:
                continue

            if curr == n:
                return temp

            visited.add(temp)

            heapq.heappush(heap, temp * 2)
            heapq.heappush(heap, temp * 3)
            heapq.heappush(heap, temp * 5)

            curr += 1