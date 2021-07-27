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
                bfs(i, graph, visited)

        return n_graph - 1


def bfs(i, graph, visited):
    queue = [i]

    while len(queue) != 0:
        node = queue.pop(0)
        visited[node] = 1

        child = graph[node]
        for i in range(len(child)):
            if visited[child[i]] == 0:
                queue.append(child[i])
