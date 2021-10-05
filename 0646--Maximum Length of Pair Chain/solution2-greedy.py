class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])

        temp = -sys.maxint
        res = 0

        for p in pairs:
            if temp < p[0]:
                temp = p[1]
                res += 1

        return res


