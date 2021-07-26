class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # dict
        dict1 = {}
        for i in range(len(s)):
            dict1[s[i]] = (dict1.get(s[i], 0) + 1) % 2

        n_odd = 0

        for key in dict1.keys():
            if dict1[key] == 1:
                n_odd += 1

        if len(s) % 2 == 0 and n_odd > 0:
            return False

        if len(s) % 2 != 0 and n_odd != 1:
            return False

        return True