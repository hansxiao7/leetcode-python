class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if i + len(needle) > len(haystack):
                    return -1
                else:
                    if haystack[i:len(needle) + i] == needle:
                        return i

        return -1




