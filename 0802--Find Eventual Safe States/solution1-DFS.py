class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # dfs
        visited = set()
        visiting = set()

        n = len(graph)

        for x in range(n):
            if x not in visited and x not in visiting:
                dfs(x, graph, visited, visiting)

        result = list(visited)
        result.sort()

        return result


def dfs(x, graph, visited, visiting):
    if x in visited:
        return True
    if x in visiting:
        return False

    visiting.add(x)

    children = graph[x]

    for i in range(len(children)):
        child = children[i]
        if dfs(child, graph, visited, visiting) is False:
            return False

    visiting.remove(x)
    visited.add(x)

    return True