class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0
        # build the graph for bus
        graph = {}
        routes = map(set, routes)
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                for stop in routes[i]:
                    if stop in routes[j]:
                        if i not in graph:
                            graph[i] = []

                        if j not in graph:
                            graph[j] = []

                        graph[i].append(j)
                        graph[j].append(i)
                        break

        # find the bus with start and end
        queue = []
        ends = set()

        for i in range(len(routes)):
            if source in routes[i]:
                queue.append((1, i))
            if target in routes[i]:
                ends.add(i)

        visited = set()
        while len(queue) != 0:
            dis, bus = queue.pop(0)

            if bus in visited:
                continue

            if bus in ends:
                return dis

            visited.add(bus)

            children = graph.get(bus, [])

            for i in range(len(children)):
                child = children[i]
                if child not in visited:
                    queue.append((dis + 1, child))

        return -1