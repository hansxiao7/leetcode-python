class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        # build the graph
        graph = {}

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
                    return []
        return result


def dfs(x, graph, result, visited, visiting):
    if x in visiting:
        return False

    if x in visited:
        return True

    visiting.add(x)

    children = graph.get(x, [])
    for i in range(len(children)):
        child = children[i]
        if dfs(child, graph, result, visited, visiting) == False:
            return False

    visiting.remove(x)
    visited.add(x)
    result.insert(0, x)

    return True