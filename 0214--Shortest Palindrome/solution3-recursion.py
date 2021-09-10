class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = s[::-1]

        m = len(s)

        i = 0
        for j in range(m - 1, -1, -1):
            if s[j] == s[i]:
                i += 1

        if i == m:
            return s

        right = s[i: m]
        return right[::-1] + self.shortestPalindrome(s[:i]) + right