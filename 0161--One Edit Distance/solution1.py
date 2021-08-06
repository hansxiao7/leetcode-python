class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                # replace
                temp1 = s[i + 1:] == t[i + 1:]
                # delete/insert
                temp2 = s[i:] == t[i + 1:]
                temp3 = s[i + 1:] == t[i:]
                return temp1 or temp2 or temp3

        if abs(len(s) - len(t)) == 1:
            return True
        else:
            return False

