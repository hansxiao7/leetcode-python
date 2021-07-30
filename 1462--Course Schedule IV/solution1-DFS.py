class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # build the graph
        graph = {}

        for edge in prerequisites:
            x = edge[0]
            y = edge[1]

            if graph.get(x) is None:
                graph[x] = [y]
            else:
                graph[x].append(y)

        # DFS search
        result = []
        for q in queries:
            x = q[0]
            target = q[1]
            visited = set()
            if dfs(x, target, graph, visited):
                result.append(True)
            else:
                result.append(False)
        return result


def dfs(x, target, graph, visited):
    if x == target:
        return True

    if graph.get(x) is None:
        return False

    visited.add(x)

    children = graph.get(x, [])

    result = False

    for i in range(len(children)):
        child = children[i]

        if child not in visited:
            result = result or dfs(child, target, graph, visited)

    return result

