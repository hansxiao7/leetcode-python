import heapq


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        dict1 = {}
        n = len(beginWord)

        for word in wordList:
            for i in range(n):
                if dict1.get(word[:i] + '*' + word[i + 1:]) is None:
                    dict1[word[:i] + '*' + word[i + 1:]] = [word]
                else:
                    dict1[word[:i] + '*' + word[i + 1:]].append(word)

        queue = [(beginWord, [beginWord])]
        result = []
        visited = set()
        path = {}

        while len(queue) != 0:
            n_q = len(queue)

            for i in range(n_q):
                word, path = queue.pop(0)

                if word == endWord:
                    result.append(path)

                visited.add(word)

                for j in range(n):
                    parent = word[:j] + '*' + word[j + 1:]
                    children = dict1.get(parent, [])

                    for child in children:
                        if child not in visited:
                            queue.append((child, path + [child]))
            if len(result) != 0:
                break

        return result

