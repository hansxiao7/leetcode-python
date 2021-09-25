class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        def encode(s):
            res = ''
            pos = 0

            while pos < len(s):
                c = s[pos]
                count = 1
                while pos + 1 < len(s) and s[pos + 1] == c:
                    count += 1
                    pos += 1

                res += c

                if count > 1:
                    res += str(count)

                pos += 1

            return res

        cache = {}

        def helper(pos, k, p, l):
            if pos + k >= len(s):
                return 0

            if k < 0:
                return sys.maxint

            if (pos, k, p, l) in cache:
                return cache[(pos, k, p, l)]

            if s[pos] == p:
                carry = int(l == 1 or l == 9 or l == 99)
                res = carry + helper(pos + 1, k, p, l + 1)
            else:
                res = 1 + helper(pos + 1, k, s[pos], 1)

            res = min(res, helper(pos + 1, k - 1, p, l))
            cache[(pos, k, p, l)] = res
            return res

        return helper(0, k, None, 0)