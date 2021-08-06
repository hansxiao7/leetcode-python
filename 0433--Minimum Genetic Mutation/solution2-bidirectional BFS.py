class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        # build graph
        graph = {}
        bank_set = set(bank)
        n = len(start)

        if end not in bank_set:
            return -1

        if start not in bank_set:
            bank.append(start)

        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                count = 0
                for k in range(n):
                    if bank[i][k] == bank[j][k]:
                        continue
                    else:
                        count += 1

                if count == 1:
                    if graph.get(bank[i]) is None:
                        graph[bank[i]] = []
                    graph[bank[i]].append(bank[j])

                    if graph.get(bank[j]) is None:
                        graph[bank[j]] = []
                    graph[bank[j]].append(bank[i])

        # BFS
        queue1 = {start}
        queue2 = {end}
        visited = set()
        step = 0

        while len(queue1) != 0 and len(queue2) != 0:
            if len(queue1) > len(queue2):
                queue1, queue2 = queue2, queue1

            s = set()

            for node in queue1:
                if node in queue2:
                    return step

                if node in visited:
                    continue

                visited.add(node)

                children = graph.get(node, [])
                for i in range(len(children)):
                    child = children[i]
                    if child not in visited:
                        s.add(child)

            queue1 = s
            step += 1

        return -1