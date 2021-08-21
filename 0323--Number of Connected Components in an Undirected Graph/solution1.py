class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = {}

        for i in range(n):
            graph[i] = i

        for edge in edges:
            x = edge[0]
            y = edge[1]
            union(x, y, graph)

        roots = set()

        for i in range(n):
            roots.add(find(i, graph))

        return len(roots)


def find(x, graph):
    p = graph[x]

    while p != graph[p]:
        p = graph[p]

    graph[x] = p
    return p


def union(x, y, graph):
    x_root = find(x, graph)
    y_root = find(y, graph)

    graph[x_root] = y_root