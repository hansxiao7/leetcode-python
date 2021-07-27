class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # Union find
        graph = {i: i for i in range(n)}
        redundant = 0

        for i in connections:
            x = i[0]
            y = i[1]
            if find(x, graph) != find(y, graph):  # union
                union(x, y, graph)
            else:
                redundant += 1

        roots = set()
        for j in range(n):
            roots.add(find(j, graph))

        if len(roots) - 1 > redundant:
            return -1
        else:
            return len(roots) - 1


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
