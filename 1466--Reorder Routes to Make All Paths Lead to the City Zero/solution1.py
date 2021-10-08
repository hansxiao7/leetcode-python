class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        maps = {}
        allConnected = {}

        for x, y in connections:
            if y not in maps:
                maps[y] = []
            maps[y].append(x)

            if x not in allConnected:
                allConnected[x] = []
            allConnected[x].append(y)

        visited = set()
        visited.add(0)
        queue = collections.deque()
        queue.append(0)

        while len(queue) != 0:
            node = queue.popleft()

            children = maps.get(node, [])

            for i in range(len(children)):
                child = children[i]
                if child not in visited:
                    visited.add(child)
                    queue.append(child)

        queue = collections.deque()
        for node in visited:
            queue.append(node)
        res = 0
        while len(queue) != 0:
            n_q = len(queue)

            for i in range(n_q):
                node = queue.popleft()

                children = maps.get(node, [])
                reverseChildren = allConnected.get(node, [])

                for j in range(len(children)):
                    child = children[j]
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)

                for j in range(len(reverseChildren)):
                    child = reverseChildren[j]
                    if child not in visited:
                        visited.add(child)
                        res += 1
                        queue.append(child)

        return res