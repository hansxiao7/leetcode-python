class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) == 1:
            return 0

        if arr[0] == arr[-1]:
            return 1

        # build graph
        graph = {}
        n = len(arr)
        for i in range(n - 1):
            for j in range(i + 1, n):

                if graph.get(i) is None:
                    graph[i] = []

                if graph.get(j) is None:
                    graph[j] = []

                if j == i + 1 or arr[j] == arr[i]:
                    graph[i].append(j)
                    graph[j].append(i)

        queue1 = {0}
        queue2 = {n - 1}
        step = 0
        visited = set()

        while len(queue1) != 0 and len(queue2) != 0:
            if len(queue1) > len(queue2):
                queue1, queue2 = queue2, queue1

            s = set()
            n_q = len(queue1)

            for i in queue1:
                if i in queue2:
                    return step
                children = graph.get(i, [])
                for j in range(len(children)):
                    child = children[j]
                    if child not in visited:
                        s.add(child)
            step += 1
            queue1 = s