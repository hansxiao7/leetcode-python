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

        visited = set()

        def helper(word, endWord):
            n = len(word)
            if word == endWord:
                return 1

            visited.add(word)
            result = sys.maxint
            for i in range(n):
                parent = word[:i] + '*' + word[i + 1:]
                children = dict1.get(parent, [])

                for j in range(len(children)):
                    child = children[j]
                    if child not in visited:
                        result = min(helper(child, endWord) + 1, result)
            visited.remove(word)
            return result

        result = helper(beginWord, endWord)
        if result == sys.maxint:
            return 0
        else:
            return result