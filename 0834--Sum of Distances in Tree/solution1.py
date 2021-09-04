class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = {}

        for x, y in edges:
            if x not in graph:
                graph[x] = []

            if y not in graph:
                graph[y] = []

            graph[x].append(y)
            graph[y].append(x)

        counts = [1] * n
        res = [0] * n

        def countHelper(curr, parent):
            children = graph.get(curr, [])
            for i in range(len(children)):
                child = children[i]
                if child == parent:
                    continue
                countHelper(child, curr)
                counts[curr] += counts[child]
                res[curr] += counts[child] + res[child]

        def helper(curr, parent):
            children = graph.get(curr, [])
            for i in range(len(children)):
                child = children[i]
                if child == parent:
                    continue
                res[child] = res[curr] - counts[child] + n - counts[child]
                helper(child, curr)

        countHelper(0, None)
        helper(0, None)

        return res
