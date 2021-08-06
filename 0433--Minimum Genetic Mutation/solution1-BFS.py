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
        queue = [(0, start)]
        visited = set()

        while len(queue) != 0:
            dis, word = queue.pop(0)

            if word in visited:
                continue

            visited.add(word)
            if word == end:
                return dis

            children = graph.get(word, [])

            for i in range(len(children)):
                child = children[i]
                if child not in visited:
                    queue.append((dis + 1, child))

        return -1
