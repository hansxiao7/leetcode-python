class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        stack = []

        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if len(stack) != 0:
                    stack.pop()
                else:
                    res += 1

        res += len(stack)
        return res