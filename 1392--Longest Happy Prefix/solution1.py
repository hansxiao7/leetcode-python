class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        pSet = set()

        temp = ''
        for c in s:
            temp = temp + c
            pSet.add(temp)

        res = ''
        temp = ''
        for i in range(len(s) - 1, 0, -1):
            c = s[i]
            temp = c + temp

            if temp in pSet:
                res = temp

        return res