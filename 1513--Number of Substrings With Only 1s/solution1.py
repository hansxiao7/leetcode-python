class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0

        start = None
        i = 0

        while i < len(s) - 1:
            if s[i] == '1':
                start = i
                while i < len(s) - 1 and s[i + 1] == '1':
                    i += 1
                result += (i - start + 2) * (i - start + 1) / 2
            i += 1
        if i != len(s):
            if s[-1] == '1':
                result += 1
        return result % (10 ** 9 + 7)
