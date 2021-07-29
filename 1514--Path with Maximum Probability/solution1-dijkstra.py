import heapq


class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        # dijkstra
        graph = [[] for _ in range(n)]

        for i in range(len(edges)):
            edge = edges[i]
            x = edge[0]
            y = edge[1]
            prob = succProb[i]

            graph[x].append([y, prob])
            graph[y].append([x, prob])

        max_prob = [0 for _ in range(n)]
        visited = set()
        heap = [(-1, start)]

        while len(heap) != 0:
            prob, node = heapq.heappop(heap)

            if node in visited:
                continue

            if node == end:
                return -prob

            visited.add(node)

            # find children
            children = graph[node]
            for i in range(len(children)):
                child, cost = children[i]
                if child not in visited and cost * prob < max_prob[child]:
                    max_prob[child] = cost * prob
                    heapq.heappush(heap, (cost * prob, child))

        return -max_prob[end]
