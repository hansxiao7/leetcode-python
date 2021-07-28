import heapq


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # Dijkstra
        # build the connections
        graph = [[0 for _ in range(n)] for _ in range(n)]
        for flight in flights:
            x = flight[0]
            y = flight[1]
            cost = flight[2]

            graph[x][y] = cost

        min_dis = [sys.maxint for _ in range(n)]
        min_dis[src] = 0

        heap = [(0, -1, src)]  # dis, stop, node

        while len(heap) != 0:
            dis, stop, node = heapq.heappop(heap)

            if stop > k:
                continue

            if node == dst:
                return dis

            for i in range(n):
                if graph[node][i] != 0:  # have connections
                    if stop + 1 <= k:
                        heapq.heappush(heap, (graph[node][i] + dis, stop + 1, i))
                        if min_dis[node] + dis < min_dis[i]:
                            min_dis[i] = min_dis[node] + dis

        if min_dis[dst] == sys.maxint:
            return -1

        return min_dis[dst]
