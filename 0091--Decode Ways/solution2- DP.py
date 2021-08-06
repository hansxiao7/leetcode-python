class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for _ in range(len(s) + 1)]

        v_1 = 1
        v_2 = 1
        result = 0
        for pos in range(len(s) - 1, -1, -1):
            if s[pos] == '0':
                result = 0
                v_2 = v_1
                v_1 = result
                continue
            result = v_1
            if pos + 2 <= len(s) and int(s[pos:pos + 2]) <= 26 and int(s[pos:pos + 2]) >= 1:
                result += v_2
            v_2 = v_1
            v_1 = result

        return result
