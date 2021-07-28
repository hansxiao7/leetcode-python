import heapq


class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # 1. use dijkstra find minimum dis
        # 2. use dfs to find number of routes

        # build the graph
        graph = {}

        for edge in edges:
            x = edge[0]
            y = edge[1]
            cost = edge[2]

            if graph.get(x) is None:
                graph[x] = [[y, cost]]
            else:
                graph[x].append([y, cost])

            if graph.get(y) is None:
                graph[y] = [[x, cost]]
            else:
                graph[y].append([x, cost])

        dis_to_last = [0 for _ in range(n + 1)]
        for start in range(1, n + 1):
            min_dis = [sys.maxint for _ in range(n + 1)]
            visited = [0 for _ in range(n + 1)]

            min_dis[start] = 0

            heap = [(0, start)]  # dis, node

            while len(heap) != 0:
                dis, node = heapq.heappop(heap)

                if visited[node] == 1:
                    continue

                visited[node] = 1
                if node == n:
                    result = dis
                    break

                # find children
                children = graph.get(node, [])
                for i in range(len(children)):
                    child, cost = children[i]
                    if visited[child] == 0 and cost + dis < min_dis[child]:
                        min_dis[child] = cost + dis
                        heapq.heappush(heap, (cost + dis, child))

            dis_to_last[start] = result
        # the minimum distances are calculated. Now find the restricted path using dfs
        return dfs(1, n, graph, dis_to_last) % 1000000007


def dfs(x, n, graph, dis_to_last):
    if x == n:
        return 1

    # find child
    result = 0
    children = graph.get(x, [])
    for i in range(len(children)):
        child, cost = children[i]
        if dis_to_last[x] > dis_to_last[child]:
            result += dfs(child, n, graph, dis_to_last)

    return result