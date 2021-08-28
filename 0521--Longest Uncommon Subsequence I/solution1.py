class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) != len(b):
            return max(len(a), len(b))

        else:
            if a == b:
                return -1
            else:
                return len(a)