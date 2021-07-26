class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0

        if len(needle) > len(haystack):
            return -1

        k = len(needle)

        needle_n = 0
        for i in range(k):
            needle_n = (needle_n * 31 + ord(needle[i])) % (10 ** 6)

        temp = 0
        for i in range(len(haystack)):
            temp = (temp * 31 + ord(haystack[i])) % (10 ** 6)
            if i >= k:
                temp = temp - ord(haystack[i - k]) * 31 ** k
                temp = temp % 10 ** 6
                if temp < 0:
                    temp += 10 ** 6

            if temp == needle_n:
                if haystack[i - k + 1:i + 1] == needle:
                    return i - k + 1

        return -1



