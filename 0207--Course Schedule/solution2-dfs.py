class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # dfs
        # build connections
        graph = {}
        n = numCourses
        for pre in prerequisites:
            if graph.get(pre[1]) is None:
                graph[pre[1]] = [pre[0]]
            else:
                graph[pre[1]].append(pre[0])

        visited = set()
        visiting = set()

        result = []

        for i in range(n):
            if i not in visited and i not in visiting:
                if dfs(i, graph, result, visited, visiting) == False:
                    return False

        return True


def dfs(x, graph, result, visited, visiting):
    if x in visited:
        return True

    if x in visiting:
        return False

    visiting.add(x)

    children = graph.get(x, [])

    for i in range(len(children)):
        child = children[i]
        if dfs(child, graph, result, visited, visiting) == False:
            return False

    visiting.remove(x)
    visited.add(x)
    result.append(x)

    return True
