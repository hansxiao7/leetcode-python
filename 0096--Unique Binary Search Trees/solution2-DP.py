class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dynamic programming
        result = [0 for _ in range(n + 1)]

        result[0] = 1
        result[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                result[i] += result[j] * result[i - 1 - j]

        return result[-1]


