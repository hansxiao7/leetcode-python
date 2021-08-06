class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = [None for _ in range(len(s) + 1)]

        def dfs(pos, s):
            if cache[pos] is not None:
                return cache[pos]

            if pos == len(s):
                result = 1
                cache[pos] = result
                return result

            if s[pos] == '0':
                cache[pos] = 0
                return 0

            result = dfs(pos + 1, s)
            if pos + 2 <= len(s) and int(s[pos:pos + 2]) <= 26 and int(s[pos:pos + 2]) >= 1:
                result += dfs(pos + 2, s)
            cache[pos] = result
            return result

        return dfs(0, s)