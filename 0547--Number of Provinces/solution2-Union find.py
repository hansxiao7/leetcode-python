class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # Union find
        n = len(isConnected)
        graph = {i: i for i in range(n)}
        roots = set()

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1 and find(i, graph) != find(j, graph):
                    union(i, j, graph)

        for i in range(n):
            roots.add(find(i, graph))
        return len(roots)


def find(x, graph):
    p = graph[x]

    while graph[p] != p:
        p = graph[p]

    graph[x] = p

    return p


def union(x, y, graph):
    root_x = find(x, graph)
    root_y = find(y, graph)

    graph[root_x] = root_y