class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        # build the graph
        graph = {}
        degree = {}
        for seq in seqs:
            for i in range(len(seq) - 1):
                if graph.get(seq[i]) is None:
                    graph[seq[i]] = [seq[i + 1]]
                else:
                    graph[seq[i]].append(seq[i + 1])
            if len(seq) == 1:
                degree[seq[0]] = 0

        # BFS
        n = len(org)

        for key in graph.keys():
            children = graph[key]

            if degree.get(key) is None:
                degree[key] = 0

            for i in range(len(children)):
                degree[children[i]] = degree.get(children[i], 0) + 1

        queue = []

        for key in degree:
            if degree[key] == 0:
                queue.append(key)

        if len(queue) != 1:
            return False

        result = []

        while len(queue) != 0:
            n_q = len(queue)
            if n_q != 1:
                return False

            node = queue.pop()  # since there is only 1 node, pop is fine
            result.append(node)

            children = graph.get(node, [])

            for i in range(len(children)):
                child = children[i]
                degree[child] -= 1
                if degree[child] == 0:
                    queue.append(child)

        if result == org and len(result) == len(degree.keys()):
            return True
        else:
            return False
