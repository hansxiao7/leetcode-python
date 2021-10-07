class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        maps1 = {}
        maps2 = {}

        for i in range(len(s)):
            if s[i] not in maps1 and t[i] not in maps2:
                maps1[s[i]] = t[i]
                maps2[t[i]] = s[i]

            elif maps1.get(s[i]) != t[i] or maps2.get(t[i]) != s[i]:
                return False

        return True