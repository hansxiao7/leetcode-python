class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # bfs
        n = numCourses
        # 建立connections
        graph = {}
        # 建立入度array
        degrees = [0 for _ in range(n)]

        for pre in prerequisites:
            degrees[pre[0]] += 1
            if graph.get(pre[1]) is None:
                graph[pre[1]] = [pre[0]]
            else:
                graph[pre[1]].append(pre[0])

        # 把入度为0的array加到queue中
        queue = []

        for i in range(n):
            if degrees[i] == 0:
                queue.append(i)

        # 建立while循环
        result = []

        while len(queue) != 0:
            node = queue.pop(0)
            result.append(node)

            children = graph.get(node, [])
            for i in range(len(children)):
                child = children[i]
                degrees[child] -= 1
                if degrees[child] == 0:
                    queue.append(child)

        if len(result) == n:
            return True
        else:
            return False
