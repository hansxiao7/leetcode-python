class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)

        def helper(node):
            if node == n - 1:
                return [[n - 1]]

            children = graph[node]

            res = []
            for i in range(len(children)):
                child = children[i]
                paths = helper(child)
                for path in paths:
                    res.append([node] + path)

            return res

        return helper(0)




