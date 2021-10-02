import heapq


class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        # MST
        # build the graph
        maps = {}
        for x, y, cost in pipes:
            if x not in maps:
                maps[x] = []
            if y not in maps:
                maps[y] = []

            maps[x].append((cost, y))
            maps[y].append((cost, x))

        visited = set()
        heap = []

        for i in range(len(wells)):
            heapq.heappush(heap, (wells[i], i + 1))

        res = 0
        while len(heap) != 0:
            cost, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            res += cost

            children = maps.get(node, [])

            for i in range(len(children)):
                newCost, newNode = children[i]
                if newNode in visited:
                    continue

                heapq.heappush(heap, children[i])

        return res