class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # DFS + cache

        def helper(s, p):
            if s == p:
                return True

            if s == '' and p == '':
                return True
            elif s == '':
                if len(p) >= 2 and p[-1] == '*':
                    return helper(s, p[:len(p) - 2])
                else:
                    return False
            elif p == '':
                return False

            result = False
            if s[-1] == p[-1] or p[-1] == '.':
                result = helper(s[:len(s) - 1], p[:len(p) - 1])
            elif p[-1] == '*':
                if len(p) >= 2:
                    result = helper(s, p[:len(p) - 2])  # 0 preceding element
                    if p[-2] == '.' or p[-2] == s[-1]:
                        result = result or helper(s[:len(s) - 1], p) or helper(s[:len(s) - 1], p[:len(
                            p) - 2])  # 1 or n preceding element
                else:
                    return False

            return result

        return helper(s, p)