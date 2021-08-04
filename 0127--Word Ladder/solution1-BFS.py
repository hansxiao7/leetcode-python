class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # build the dict
        dict1 = {}
        n = len(beginWord)
        for word in wordList:
            for i in range(n):
                if dict1.get(word[:i] + '*' + word[i + 1:]) is None:
                    dict1[word[:i] + '*' + word[i + 1:]] = [word]
                else:
                    dict1[word[:i] + '*' + word[i + 1:]].append(word)

        queue = [beginWord]
        result = 1
        visited = set()

        while len(queue) != 0:
            n_q = len(queue)
            for i in range(n_q):
                node = queue.pop(0)
                if node == endWord:
                    return result
                visited.add(node)

                for j in range(n):
                    parent = node[:j] + '*' + node[j + 1:]
                    children = dict1.get(parent, [])

                    for k in range(len(children)):
                        child = children[k]
                        if child not in visited:
                            queue.append(child)

            result += 1
        return 0