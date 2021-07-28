class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # BFS
        # build the connections
        graph = {}
        for t in times:
            if graph.get(t[0]) is None:
                graph[t[0]] = [[t[1], t[2]]]
            else:
                graph[t[0]].append([t[1], t[2]])
        queue = [k]
        min_time = [sys.maxint for _ in range(n + 1)]
        min_time[k] = 0
        min_time[0] = 0

        while len(queue) != 0:
            n = len(queue)
            for i in range(n):
                node = queue.pop()
                children = graph.get(node, [])

                for child in children:
                    pos = child[0]
                    time = child[1]
                    if time + min_time[node] < min_time[pos]:
                        queue.append(pos)
                        min_time[pos] = time + min_time[node]
        result = max(min_time)
        if result == sys.maxint:
            return -1
        return result

