class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []

        def helper(pos, s, curr, k):
            if pos >= len(s):
                return
            if k == 0:
                if s[pos] == '0':
                    if pos != len(s) - 1:
                        return
                    else:
                        curr += '0'
                        result.append(curr)
                        return
                elif int(s[pos:]) > 0 and int(s[pos:]) <= 255:
                    curr += s[pos:]
                    result.append(curr)
                else:
                    return

            if s[pos] == '0':
                helper(pos + 1, s, curr + '0.', k - 1)
            else:
                temp1 = int(s[pos])
                helper(pos + 1, s, curr + s[pos] + '.', k - 1)

                if pos + 1 <= len(s):
                    helper(pos + 2, s, curr + s[pos:pos + 2] + '.', k - 1)
                if pos + 2 <= len(s):
                    temp2 = int(s[pos:pos + 3])
                    if temp2 <= 255:
                        helper(pos + 3, s, curr + s[pos:pos + 3] + '.', k - 1)

        helper(0, s, '', 3)
        return result