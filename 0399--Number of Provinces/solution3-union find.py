class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # union find
        graph = {}

        for i in range(len(equations)):
            eq = equations[i]
            rank = values[i]
            x = eq[0]
            y = eq[1]

            if graph.get(x) is None and graph.get(y) is None:
                graph[x] = [y, rank]
                graph[y] = [y, 1]
            elif graph.get(x) is None:
                graph[x] = [y, rank]
                union(x, y, rank, graph)
            elif graph.get(y) is None:
                graph[y] = [x, 1. / rank]
                union(x, y, rank, graph)
            else:
                union(x, y, rank, graph)

        result = []
        for q in queries:
            x = q[0]
            y = q[1]

            if graph.get(x) and graph.get(y):
                x_root, x_val = find(x, graph)
                y_root, y_val = find(y, graph)
                if x_root == y_root:
                    temp = x_val / y_val

                else:
                    temp = -1
            else:
                temp = -1

            result.append(temp)

        return result


def find(x, graph):  # graph[x] = [y, rank]
    p, val = graph[x]

    while graph[p][0] != p:
        val = val * graph[p][1]
        p = graph[p][0]

    graph[x] = [p, val]

    return p, val


def union(x, y, factor, graph):  # x / y = factor
    x_root, x_val = find(x, graph)
    y_root, y_val = find(y, graph)

    graph[x_root] = [y_root, factor * y_val / x_val]

