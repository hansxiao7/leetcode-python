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

        # set rank and res, run dfs
        ranks = {}
        res = set()

        def helper(node, maxRank, parent):
            if node in ranks:
                return ranks[node]

            ranks[node] = maxRank

            children = graph.get(node, [])

            for i in range(len(children)):
                child = children[i]
                if child == parent:
                    continue

                childRank = helper(child, maxRank + 1, node)

                if childRank == maxRank + 1:
                    res.add((node, child))
                else:
                    ranks[node] = min(childRank, ranks[node])

            return ranks[node]

        helper(0, 0, None)
        return res
