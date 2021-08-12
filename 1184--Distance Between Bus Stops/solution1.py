import heapq


class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        # BFS
        heap = [(0, start)]
        visited = set()

        while len(heap) != 0:
            dis, node = heapq.heappop(heap)
            if node in visited:
                continue

            if node == destination:
                return dis

            visited.add(node)

            l = node - 1
            if l < 0:
                l = len(distance) - 1
            r = node + 1
            if r >= len(distance):
                r = 0

            if l not in visited:
                left_dis = distance[l]
                heapq.heappush(heap, (left_dis + dis, l))

            if r not in visited:
                right_dis = distance[node]
                heapq.heappush(heap, (right_dis + dis, r))


