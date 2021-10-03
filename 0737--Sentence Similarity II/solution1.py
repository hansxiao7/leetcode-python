class Solution(object):
    def areSentencesSimilarTwo(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        if len(sentence1) != len(sentence2):
            return False
        graph = {}

        def find(x):
            p = graph[x]

            while p != graph[p]:
                p = graph[p]

            graph[x] = p

            return p

        def union(x, y):
            x_root = find(x)
            y_root = find(y)

            graph[x_root] = y_root

        for x, y in similarPairs:
            if x not in graph:
                graph[x] = x
            if y not in graph:
                graph[y] = y

            union(x, y)

        for i in range(len(sentence1)):
            x = sentence1[i]
            y = sentence2[i]

            if x == y:
                continue

            if x not in graph or y not in graph:
                return False

            if find(x) != find(y):
                return False

        return True