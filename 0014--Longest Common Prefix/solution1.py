class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_l = sys.maxint
        for i in strs:
            if len(i) < min_l:
                min_l = len(i)

        result = ''
        for i in range(min_l):
            temp = strs[0][i]
            for s in strs:
                if s[i] != temp:
                    return result
            result += temp

        return result