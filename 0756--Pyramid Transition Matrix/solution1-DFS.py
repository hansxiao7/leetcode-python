class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        # use rabin-karp
        graph = {}

        pow = 31
        mod = 10 ** 6

        for a in allowed:
            x = a[:2]
            y = a[2]

            if x not in graph:
                graph[x] = set()

            graph[x].add(y)

        def helper(curr, pos, nextLayer, layer):
            if layer == -1:
                return True

            if pos == layer:
                return helper(nextLayer, 0, '', layer - 1)

            temp = curr[pos] + curr[pos + 1]

            children = graph.get(temp, set())

            for child in children:
                temp = helper(curr, pos + 1, nextLayer + child, layer)

                if temp:
                    return True

            return False

        return helper(bottom, 0, '', len(bottom) - 1)
