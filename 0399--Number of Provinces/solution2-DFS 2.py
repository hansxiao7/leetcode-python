class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # dfs with graph
        dict1 = {}
        n = 0

        for i in range(len(equations)):
            x = equations[i][0]
            if dict1.get(x) is None:
                dict1[x] = n
                n += 1

            y = equations[i][1]
            if dict1.get(y) is None:
                dict1[y] = n
                n += 1

        graph = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(len(equations)):
            eq = equations[i]
            x = dict1[eq[0]]
            y = dict1[eq[1]]
            graph[x][y] = values[i]
            graph[y][x] = 1. / values[i]

        result = []
        for q in queries:
            visited = set()
            if dict1.get(q[0]) is None or dict1.get(q[1]) is None:
                result.append(-1)
                continue
            else:
                x = dict1[q[0]]
                y = dict1[q[1]]
                temp = dfs(x, y, graph, visited)
                if temp == 0:
                    temp = -1
                result.append(temp)

        return result


def dfs(x, y, graph, visited):
    n = len(graph)
    if x in visited:
        return 0
    if graph[x][y] != 0:
        return graph[x][y]

    result = 0
    visited.add(x)
    for i in range(n):
        if graph[x][i] != 0:
            result = graph[x][i] * dfs(i, y, graph, visited)
        if result != 0:
            break

    return result

