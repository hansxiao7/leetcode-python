class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        depth = 0

        for c in s:
            if c == '(':
                stack.append('(')
            elif c == ')':
                depth = max(depth, len(stack))
                stack.pop()

        return depth