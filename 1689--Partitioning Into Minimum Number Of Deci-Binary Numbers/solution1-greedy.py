class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        res = 0
        for c in n:
            if c != '0':
                res = max(res, int(c))

        return res