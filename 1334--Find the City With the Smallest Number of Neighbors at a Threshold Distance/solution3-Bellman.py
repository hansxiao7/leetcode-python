class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # bellman
        dis_graph = [[sys.maxint for _ in range(n)] for _ in range(n)]  # start, end

        min_n = sys.maxint

        for start in range(n):
            dis_graph[start][start] = 0

            for k in range(1, n):
                for edge in edges:
                    x = edge[0]
                    y = edge[1]
                    cost = edge[2]

                    dis_graph[start][x] = min(dis_graph[start][x], dis_graph[start][y] + cost)
                    dis_graph[start][y] = min(dis_graph[start][y], dis_graph[start][x] + cost)

            temp = 0
            for i in range(n):
                if dis_graph[start][i] <= distanceThreshold and i != start:
                    temp += 1

            if temp <= min_n:
                min_n = temp
                result = start
        return result

