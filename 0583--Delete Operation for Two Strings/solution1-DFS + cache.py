class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # DFS
        cache = {}

        def helper(s1, s2):
            if cache.get((s1, s2)):
                return cache[(s1, s2)]
            if s1 == '' or s2 == '':
                result = max(len(s1), len(s2))
                cache[(s1, s2)] = result
                return result

            if s1[-1] == s2[-1]:
                result = helper(s1[:len(s1) - 1], s2[:len(s2) - 1])
            else:
                result = min(helper(s1, s2[:len(s2) - 1]), helper(s1[:len(s1) - 1], s2)) + 1
            cache[(s1, s2)] = result
            return result

        return helper(word1, word2)