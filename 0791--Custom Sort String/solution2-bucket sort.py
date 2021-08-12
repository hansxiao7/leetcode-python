class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        # bucket sort
        counts = {}

        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1

        result = ''
        for c in order:
            result += c * counts.get(c, 0)
            counts[c] = 0

        for key in counts.keys():
            result += key * counts[key]

        return result
