import heapq


class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # dijkstra
        graph = [[0 for _ in range(n)] for _ in range(n)]

        for edge in edges:
            x = edge[0]
            y = edge[1]
            cost = edge[2]

            graph[x][y] = cost
            graph[y][x] = cost

        min_length = sys.maxint
        result = -1

        for start in range(n):
            neighbors = []
            visited = [0 for _ in range(n)]

            heap = [(0, start)]  # dis, node

            while len(heap) != 0:
                dis, node = heapq.heappop(heap)
                if visited[node] == 1:
                    continue
                visited[node] = 1
                if node != start:
                    neighbors.append(node)

                # find neighbors
                for i in range(n):
                    if graph[node][i] != 0:  # have neighbors
                        if visited[i] == 0 and dis + graph[node][i] <= distanceThreshold:  # not visited
                            heapq.heappush(heap, (dis + graph[node][i], i))

            if len(neighbors) <= min_length:
                min_length = len(neighbors)
                result = start

        return result