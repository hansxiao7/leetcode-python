class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        # build suffix

        suffix = [0] * len(needle)

        for i in range(1, len(needle)):
            j = suffix[i - 1]

            while j > 0 and needle[i] != needle[j]:
                j = suffix[j - 1]

            suffix[i] = j + (needle[i] == needle[j])

        # compare needle and target
        dp = [0] * len(haystack)

        for i in range(len(haystack)):
            j = dp[i - 1]

            while j > 0 and haystack[i] != needle[j]:
                j = suffix[j - 1]

            dp[i] = j + (haystack[i] == needle[j])

            if dp[i] == len(needle):
                return i - len(needle) + 1

        return -1