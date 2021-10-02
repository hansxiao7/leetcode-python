import heapq


class Solution(object):
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # build maps
        maps = {}

        for x, y, val in connections:
            if x not in maps:
                maps[x] = []
            if y not in maps:
                maps[y] = []

            maps[x].append((val, y))
            maps[y].append((val, x))

        visited = set()
        visited.add(1)
        heap = []

        children = maps.get(1, [])

        for i in range(len(children)):
            child = children[i]
            heapq.heappush(heap, child)

        res = 0
        while len(heap) != 0:
            val, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            res += val

            children = maps.get(node, [])

            for i in range(len(children)):
                newVal, newNode = children[i]
                if newNode in visited:
                    continue

                heapq.heappush(heap, (newVal, newNode))

        if len(visited) == n:
            return res
        return -1
