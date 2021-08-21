import heapq


class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        heap = []

        # build graph
        graph = {}
        for r in roads:
            x = r[0]
            y = r[1]
            cost = r[2]

            if x not in graph:
                graph[x] = []
            graph[x].append((y, cost))
            if y not in graph:
                graph[y] = []
            graph[y].append((x, cost))

        heap.append((0, 0))

        target = n - 1

        result = 0
        minDis = [sys.maxint for _ in range(n)]
        minDis[0] = 0
        counts = [0 for _ in range(n)]
        counts[0] = 1

        while len(heap) != 0:
            dis, node = heapq.heappop(heap)

            if dis > minDis[node]:
                continue

            children = graph.get(node, [])

            for i in range(len(children)):
                child, cost = children[i]

                if dis + cost < minDis[child]:
                    minDis[child] = dis + cost
                    counts[child] = counts[node]
                    heapq.heappush(heap, (dis + cost, child))
                elif dis + cost == minDis[child]:
                    counts[child] += counts[node]

        return counts[n - 1] % (10 ** 9 + 7)