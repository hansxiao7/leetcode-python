class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n - 1:
            return -1

        # build graph
        graph = [[] for _ in range(n)]
        for i in range(len(connections)):
            x = connections[i][0]
            y = connections[i][1]
            graph[x].append(y)
            graph[y].append(x)

        n_graph = 0
        visited = [0 for _ in range(n)]

        for i in range(n):
            if visited[i] == 0:
                n_graph += 1
                dfs(i, visited, graph)

        return n_graph - 1


def dfs(i, visited, graph):
    if visited[i] == 1:
        return
    visited[i] = 1
    for j in range(len(graph[i])):
        if visited[graph[i][j]] == 0:
            dfs(graph[i][j], visited, graph)

