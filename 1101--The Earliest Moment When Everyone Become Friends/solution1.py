class Solution(object):
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int
        """
        count = n
        graph = {}

        logs.sort()

        for log in logs:
            t = log[0]
            x = log[1]
            y = log[2]

            if x not in graph:
                graph[x] = x
            if y not in graph:
                graph[y] = y

            if find(x, graph) != find(y, graph):
                union(x, y, graph)
                count -= 1

            if count == 1:
                return t

        return -1


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