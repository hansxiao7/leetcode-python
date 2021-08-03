class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        cache = {}

        def dfs(a, b):
            if cache.get((a, b)):
                return cache[(a, b)]

            if a == '' or b == '':
                cache[(a, b)] = max(len(a), len(b))
                return max(len(a), len(b))

            if a[-1] == b[-1]:
                result = dfs(a[:len(a) - 1], b[:len(b) - 1])
            else:
                temp1 = 1 + dfs(a[:len(a) - 1], b)  # del a
                temp2 = 1 + dfs(a, b[:len(b) - 1])  # del b
                temp3 = 1 + dfs(a[:len(a) - 1], b[:len(b) - 1])  # replace

                result = min(temp1, temp2, temp3)
            cache[(a, b)] = result
            return result

        return dfs(word1, word2)