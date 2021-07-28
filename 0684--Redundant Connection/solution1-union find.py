class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Union find
        n = len(edges)
        graph = {i: i for i in range(1, n + 1)}

        for i in range(n):
            edge = edges[i]
            x = edge[0]
            y = edge[1]

            if find(x, graph) == find(y, graph):
                return edge
            else:
                union(x, y, graph)


def find(x, graph):
    p = graph[x]

    while graph[p] != p:
        p = graph[p]

    graph[x] = p

    return p


def union(x, y, graph):
    x_root = find(x, graph)
    y_root = find(y, graph)

    graph[x_root] = y_root