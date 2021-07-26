class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        # use Rabin-Karp

        power = 32
        mod = 10 ** 6
        p_r = 1

        l = 0
        r = 0

        start = 0

        for i in range(len(s)):
            l = l * power + ord(s[i])
            l = l % mod
            r = r + ord(s[i]) * p_r
            r = r % mod

            if l == r:
                start = i + 1

            p_r = p_r * power
        result = s
        if start < len(s):
            for i in range(start, len(s)):
                result = s[i] + result
        else:
            return result

        return result