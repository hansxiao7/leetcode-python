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

        # bfs
        # create an array to store in-degrees
        degree = [0 for _ in range(n)]

        for pre in prerequisites:
            degree[pre[0]] += 1
            if graph.get(pre[1]) is None:
                graph[pre[1]] = [pre[0]]
            else:
                graph[pre[1]].append(pre[0])

        # find the elements with 0 in-degrees
        queue = []

        for i in range(n):
            if degree[i] == 0:
                queue.append(i)

        # start iteration
        result = []

        while len(queue) != 0:
            node = queue.pop(0)
            result.append(node)

            children = graph.get(node, [])
            for i in range(len(children)):
                child = children[i]
                degree[child] -= 1
                if degree[child] == 0:
                    queue.append(child)

        if len(result) == n:
            return result
        else:
            return []