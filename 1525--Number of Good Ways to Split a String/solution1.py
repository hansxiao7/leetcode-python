class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """

        temp = set()
        left = [0] * len(s)
        for i in range(len(s) - 1):
            temp.add(s[i])
            left[i] = len(temp)

        temp = set()
        right = [0] * len(s)
        for i in range(len(s) - 1, 0, -1):
            temp.add(s[i])
            right[i] = len(temp)

        res = 0
        for i in range(len(s) - 1):
            if left[i] == right[i + 1]:
                res += 1

        return res