class Solution(object):
    def minimumSemesters(self, n, relations):
        """
        :type n: int
        :type relations: List[List[int]]
        :rtype: int
        """
        # BFS
        # build the graph
        graph = {}

        for edge in relations:
            x = edge[0] - 1
            y = edge[1] - 1

            if graph.get(x) is None:
                graph[x] = [y]

            else:
                graph[x].append(y)

        # build the in-degree array
        degree = [0 for _ in range(n)]

        for key in graph.keys():
            children = graph[key]

            for i in range(len(children)):
                degree[children[i]] += 1

        queue = []

        for i in range(n):
            if degree[i] == 0:
                queue.append(i)

        result = 0
        course = []

        while len(queue) != 0:
            n_q = len(queue)

            for i in range(n_q):
                node = queue.pop(0)
                course.append(node)

                children = graph.get(node, [])

                for j in range(len(children)):
                    child = children[j]
                    degree[child] -= 1
                    if degree[child] == 0:
                        queue.append(child)

            result += 1

        if len(course) != n:
            return -1

        return result