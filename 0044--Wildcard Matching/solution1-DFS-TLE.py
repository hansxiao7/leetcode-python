class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        cache = {}

        def helper(s, p):
            if cache.get((s, p)):
                return cache[(s, p)]
            if s == '' and p == '':
                return True
            elif s == '':
                if p[-1] == '*':
                    result = helper(s, p[:len(p) - 1])
                else:
                    result = False
                cache[(s, p)] = result
                return result
            elif p == '':
                return False

            result = False
            if p[-1] == s[-1] or p[-1] == '?':
                result = result or helper(s[:len(s) - 1], p[:len(p) - 1])
            elif p[-1] == '*':
                result = result or helper(s[:len(s) - 1], p)  # non-empty
                result = result or helper(s, p[:len(p) - 1])  # empty
            cache[(s, p)] = result
            return result

        return helper(s, p)