class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        pow = 31
        mod = 10 ** 6

        def checkVal(l):
            if l == 0:
                return True, ''
            maps = {}

            temp = 0
            tempStr = collections.deque()
            for i in range(l):
                temp = temp * pow + ord(s[i])
                temp = temp % mod
                tempStr.append(s[i])

            maps[temp] = 0

            for i in range(l, len(s)):
                topVal = ord(s[i - l]) * pow ** (l - 1)
                topVal = topVal % mod

                temp -= topVal
                if temp < 0:
                    temp += mod

                tempStr.popleft()
                tempStr.append(s[i])

                temp = temp * pow + ord(s[i])
                temp = temp % mod
                if temp in maps:
                    pos = maps[temp]
                    if s[pos: pos + l] == s[i + 1 - l:i + 1]:
                        return True, ''.join(tempStr)
                maps[temp] = i - l + 1
            return False, None

        left = 0
        right = len(s) - 1

        while left < right:
            mid = (left + right) // 2
            res, tempStr = checkVal(mid)
            if res:
                left = mid + 1
            else:
                right = mid

        res, tempStr = checkVal(left)
        if res:
            return tempStr

        res, tempStr = checkVal(left - 1)
        if res:
            return tempStr