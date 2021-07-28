class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # floyd
        # build the graph
        graph = [[sys.maxint for _ in range(n)] for _ in range(n)]

        for edge in edges:
            x = edge[0]
            y = edge[1]
            cost = edge[2]

            graph[x][y] = cost
            graph[y][x] = cost

        # floyd
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i != j and j != k:
                        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        min_n = sys.maxint
        for i in range(n):
            temp = 0
            for j in range(n):
                if graph[i][j] <= distanceThreshold:
                    temp += 1

            if temp <= min_n:
                min_n = temp
                result = i

        return result