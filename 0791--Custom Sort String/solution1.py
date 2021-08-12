class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        dict1 = {}
        for i in range(len(order)):
            dict1[order[i]] = i

        s = list(s)
        s.sort(key=lambda x: dict1.get(x, sys.maxint))
        s = ''.join(s)

        return s