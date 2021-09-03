class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = list(s)

        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)

            elif s[i] == ')':
                if len(stack) != 0:
                    stack.pop()
                else:
                    res[i] = ''

        for i in range(len(stack)):
            res[stack[i]] = ''
        return ''.join(res)