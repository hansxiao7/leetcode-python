class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        # build the graph
        n = len(quiet)
        graph = {}
        for edge in richer:
            x = edge[0]
            y = edge[1]

            if graph.get(y) is None:
                graph[y] = [x]
            else:
                graph[y].append(x)

        # build the dict for quietness
        quiet_dict = {}
        for i in range(n):
            quiet_dict[i] = quiet[i]

        answer = []

        for i in range(n):
            visited = set()
            visiting = set()

            result = []

            temp = dfs(i, graph, visited, visiting, result)

            if temp is False:
                # the richer is wrong
                return []

            result.sort(key=lambda x: quiet_dict[x])
            answer.append(result[0])

        return answer


def dfs(x, graph, visited, visiting, result):
    if x in visiting:
        return False

    if x in visited:
        return True

    visiting.add(x)

    children = graph.get(x, [])

    for i in range(len(children)):
        child = children[i]
        if child not in visited:
            temp = dfs(child, graph, visited, visiting, result)
            if temp is False:
                return False

    visited.add(x)
    visiting.remove(x)

    result.append(x)

    return True