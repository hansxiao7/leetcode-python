class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # build the graph
        word_li = []
        graph = {}

        for word in words:
            for i in range(len(word)):
                word_li.append(word[i])

        for i in range(len(words) - 1):
            curr = words[i]
            next = words[i + 1]

            n = min(len(curr), len(next))
            if curr[:n] == next[:n] and len(curr) > len(next):
                return ''

            for j in range(n):
                if curr[j] == next[j]:
                    continue
                else:
                    if graph.get(curr[j]) is None:
                        graph[curr[j]] = [next[j]]
                    else:
                        graph[curr[j]].append(next[j])
                    break

        # bfs - topology sort
        # build the array for in-degrees
        degree = {}
        print(graph)
        for i in range(len(word_li)):
            degree[word_li[i]] = 0

        for key in graph.keys():
            children = graph[key]
            for child in children:
                degree[child] += 1

        queue = []

        for key in degree:
            if degree[key] == 0:
                queue.append(key)

        result = ''
        while len(queue) != 0:
            node = queue.pop()
            result = result + node

            children = graph.get(node, [])
            for i in range(len(children)):
                child = children[i]
                if degree[child] > 0:
                    degree[child] -= 1
                    if degree[child] == 0:
                        queue.append(child)

        if len(result) == len(degree.keys()):
            return result
        else:
            return ''