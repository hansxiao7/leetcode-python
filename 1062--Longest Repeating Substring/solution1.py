class Solution(object):
    def longestRepeatingSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = 10 ** 7
        pow = 31

        def checkVal(l):
            if l == 0:
                return True
            maps = {}

            temp = 0

            for i in range(l):
                temp = temp * pow + ord(s[i])
                temp = temp % mod

            maps[temp] = 0

            for i in range(l, len(s)):
                topVal = ord(s[i - l]) * pow ** (l - 1)
                topVal = topVal % mod

                temp = (temp - topVal + mod) % mod

                temp = temp * pow + ord(s[i])
                temp = temp % mod
                if temp in maps:
                    pos = maps[temp]
                    if s[pos: pos + l] == s[i - l + 1:i + 1]:
                        return True
                maps[temp] = i - l + 1

            return False

        left = 0
        right = len(s) - 1

        while left < right:
            mid = (left + right) // 2
            if checkVal(mid):
                left = mid + 1
            else:
                right = mid

        if checkVal(left):
            return left
        return left - 1