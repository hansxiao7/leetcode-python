import heapq


class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        heap = []
        visited = set()
        heap.append((informTime[headID], headID))

        # build graph
        graph = {}
        for i in range(len(manager)):
            if manager[i] == -1:
                continue

            if manager[i] not in graph:
                graph[manager[i]] = []

            graph[manager[i]].append(i)

        visited.add(headID)
        result = 0
        while len(heap) != 0:
            t, node = heap.pop(0)
            result = max(result, t)
            visited.add(node)
            children = graph.get(node, [])

            for i in range(len(children)):
                child = children[i]
                if child not in visited:
                    heap.append((t + informTime[child], child))
                    visited.add(child)

        return result