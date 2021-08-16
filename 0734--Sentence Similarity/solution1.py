class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        if len(sentence1) != len(sentence2):
            return False

        graph = {}

        for p in similarPairs:
            x = p[0]
            y = p[1]

            if x not in graph:
                graph[x] = set()
            if y not in graph:
                graph[y] = set()

            graph[x].add(y)
            graph[y].add(x)

        n = len(sentence1)

        for i in range(n):
            if sentence1[i] == sentence2[i]:
                continue
            elif sentence1[i] in graph and sentence2[i] in graph[sentence1[i]]:
                continue
            else:
                return False

        return True
