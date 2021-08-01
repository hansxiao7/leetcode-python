import heapq


class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        # djikstra
        # build graph
        graph = [[] for _ in range(n + 1)]
        for edge in pipes:
            x = edge[0]
            y = edge[1]
            cost = edge[2]

            graph[x].append([y, cost])
            graph[y].append([x, cost])

        result = 0
        visited = set()
        heap = []

        for i in range(n):
            heapq.heappush(heap, (wells[i], i + 1))

        while len(heap) != 0:
            val, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)

            if val > wells[node - 1]:
                result += wells[node - 1]
            else:
                result += val

            children = graph[node]

            for i in range(len(children)):
                child, p_cost = children[i]

                if child not in visited:
                    heapq.heappush(heap, (p_cost, child))

        return result

