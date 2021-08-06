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

        queue = [(0, 0)]
        visited = set()

        while len(queue) != 0:

            dis, node = queue.pop(0)

            if node in visited:
                continue

            if node == n - 1:
                return dis

            visited.add(node)

            children = graph.get(node, [])
            for i in range(len(children)):
                child = children[i]
                if child not in visited:
                    queue.append((1 + dis, child))


