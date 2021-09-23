class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        # build the graph
        graph = {}

        for x, y in connections:
            if x not in graph:
                graph[x] = []

            if y not in graph:
                graph[y] = []

            graph[x].append(y)
            graph[y].append(x)

        # set the timestamp and minStamp
        times = [-1] * n
        minStamp = [-1] * n

        res = []
        self.time = -1

        def helper(node, parent):

            self.time += 1
            time = self.time
            times[node] = time
            minStamp[node] = time
            children = graph.get(node, [])

            for i in range(len(children)):
                child = children[i]
                if child == parent:
                    continue

                if times[child] == -1:
                    helper(child, node)
                    if times[child] == minStamp[child]:
                        res.append([node, child])
                minStamp[node] = min(minStamp[node], minStamp[child])

        helper(0, 0)
        return res