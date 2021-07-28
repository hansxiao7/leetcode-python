class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        result = []
        for i in range(len(queries)):
            visited = set()
            x = queries[i][0]
            y = queries[i][1]
            temp = dfs(x, y, equations, values, visited)
            if temp == 0:
                result.append(-1)
            else:
                result.append(temp)

        return result


def dfs(x, y, equations, values, visited):
    if x in visited:
        return 0

    visited.add(x)
    result = 0

    for i in range(len(equations)):
        if equations[i] == [x, y]:
            return values[i]
        elif equations[i] == [y, x]:
            return 1. / values[i]
        else:
            if equations[i][0] == x:
                result = values[i] * dfs(equations[i][1], y, equations, values, visited)
            elif equations[i][1] == x:
                result = 1. / values[i] * dfs(equations[i][0], y, equations, values, visited)
            elif equations[i][0] == y:
                result = 1. / values[i] * dfs(x, equations[i][1], equations, values, visited)
            elif equations[i][1] == y:
                result = values[i] * dfs(x, equations[i][0], equations, values, visited)
        if result != 0:
            break
    return result
