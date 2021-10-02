class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        graph = {}

        def find(x):
            p = graph[x]

            while p != graph[p]:
                p = graph[p]

            graph[x] = p

            return p

        def union(x, y):
            x_root = find(x)
            y_root = find(y)

            graph[y_root] = x_root

        for i in range(n):
            pipes.append((0, i + 1, wells[i]))

        pipes.sort(key=lambda x: x[2])

        res = 0
        for x, y, cost in pipes:
            if x not in graph:
                graph[x] = x
            if y not in graph:
                graph[y] = y
            if find(x) == find(y):
                continue

            union(x, y)
            res += cost

        return res