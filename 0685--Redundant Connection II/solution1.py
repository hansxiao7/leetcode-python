class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        for m in range(len(edges) - 1, -1, -1):
            edge = edges[m]
            graph = {}
            flag = True

            for edge2 in edges:
                if edge2 != edge:
                    x = edge2[0]
                    y = edge2[1]
                    if x not in graph:
                        graph[x] = []
                    graph[x].append(y)

            # topological sort
            indegree = [0 for _ in range(n + 1)]
            for key in graph:
                children = graph[key]
                for child in children:
                    indegree[child] += 1

            queue = []
            for i in range(1, n + 1):
                if indegree[i] == 0:
                    queue.append(i)
                if indegree[i] > 1:
                    flag = False
                    break

            if not flag:
                continue

            if len(queue) > 1:
                continue

            result = []
            while len(queue) != 0:
                node = queue.pop(0)
                children = graph.get(node, [])
                result.append(node)
                for i in range(len(children)):
                    child = children[i]
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        queue.append(child)

            if len(result) != n:
                continue

            return edge