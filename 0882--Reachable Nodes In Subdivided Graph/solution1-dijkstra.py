import heapq


class Solution(object):
    def reachableNodes(self, edges, maxMoves, n):
        """
        :type edges: List[List[int]]
        :type maxMoves: int
        :type n: int
        :rtype: int
        """
        # DFS
        graph = [[] for _ in range(n)]

        for edge in edges:
            x = edge[0]
            y = edge[1]
            cost = edge[2]

            graph[x].append([y, cost + 1])
            graph[y].append([x, cost + 1])

        visited = set()
        HP = [-sys.maxint for _ in range(n)]
        HP[0] = maxMoves
        min_dis = [sys.maxint for _ in range(n)]
        min_dis[0] = 0

        heap = [(0, 0)]  # dis, node

        while len(heap) != 0:
            dis, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            # find children
            children = graph[node]
            for i in range(len(children)):
                child, cost = children[i]
                if child not in visited and cost + dis < min_dis[child]:
                    min_dis[child] = cost + dis
                    HP[child] = HP[node] - cost
                    heapq.heappush(heap, (cost + dis, child))

        result = 0
        print(HP)

        for i in range(n):
            if HP[i] >= 0:
                result += 1

        for edge in edges:
            x = edge[0]
            y = edge[1]
            mid = edge[2]

            if HP[x] >= 0 and HP[y] >= 0:
                result += min(mid, HP[y] + HP[x])
            elif HP[x] >= 0:
                result += min(mid, HP[x])
            elif HP[y] >= 0:
                result += min(mid, HP[y])

        return result