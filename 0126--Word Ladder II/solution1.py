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

        queue = [beginWord]
        visited = set()
        path = {}
        depth = 1
        flag = False

        while len(queue) != 0:
            n_q = len(queue)

            for i in range(n_q):
                word = queue.pop(0)
                if word != endWord:
                    visited.add(word)
                else:
                    flag = True
                    break

                for j in range(n):
                    parent = word[:j] + '*' + word[j + 1:]
                    children = dict1.get(parent, [])

                    for child in children:
                        if child not in visited:
                            queue.append(child)
                            if path.get(child) is None:
                                path[child] = set()
                            path[child].add(word)
            if flag:
                break
            depth += 1

        if flag is False:
            return []

        result = []
        curr = []

        def helper(word, curr):
            if len(curr) > depth - 1:
                return
            if word == beginWord:
                temp = list(curr) + [beginWord]
                temp.reverse()
                result.append(temp)
                return

            curr.append(word)
            parents = list(path.get(word, set()))
            for parent in parents:
                helper(parent, curr)
            curr.pop()

        helper(endWord, curr)

        return result

