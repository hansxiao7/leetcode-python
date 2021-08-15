class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        dict1 = {}

        for i in range(len(word)):
            if word[i] not in dict1:
                dict1[word[i]] = []
            dict1[word[i]].append(i)

        result = 0
        for pattern in patterns:
            if pattern[0] not in dict1:
                continue

            pos = dict1[pattern[0]]
            for i in range(len(pos)):
                if word[pos[i]:pos[i] + len(pattern)] == pattern:
                    result += 1
                    break

        return result