class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = [-1] * len(s)

        def helper(pos):
            if pos == len(s):
                return 1

            if cache[pos] != -1:
                return cache[pos]

            if s[pos] == '0':
                cache[pos] = 0
                return 0
            res = 0
            if s[pos] == '*':
                res += 9 * helper(pos + 1)
            else:
                res += helper(pos + 1)

            if pos + 1 < len(s):
                if s[pos] == '*':
                    if s[pos + 1] != '*':
                        temp = int(s[pos + 1])
                        if temp <= 6:
                            res += 2 * helper(pos + 2)
                        else:
                            res += helper(pos + 2)
                    else:
                        res += 15 * helper(pos + 2)
                else:
                    if int(s[pos]) <= 2:
                        if s[pos + 1] != '*':
                            if int(s[pos] + s[pos + 1]) <= 26:
                                res += helper(pos + 2)
                        else:
                            if int(s[pos]) == 1:
                                res += 9 * helper(pos + 2)
                            else:
                                res += 6 * helper(pos + 2)

            cache[pos] = res % (10 ** 9 + 7)
            return res % (10 ** 9 + 7)

        return helper(0) % (10 ** 9 + 7)
