class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = {}

        for i in range(n):
            graph[i] = i

        for edge in edges:
            x = edge[0]
            y = edge[1]

            if find(x, graph) != find(y, graph):
                union(x, y, graph)
            else:
                return False

        roots = set()
        for i in range(n):
            roots.add(find(i, graph))

        if len(roots) != 1:
            return False
        else:
            return True


def find(x, graph):
    p = graph[x]

    if p != graph[p]:
        p = graph[p]

    graph[x] = p

    return p


def union(x, y, graph):
    x_root = find(x, graph)
    y_root = find(y, graph)

    graph[y_root] = x_root