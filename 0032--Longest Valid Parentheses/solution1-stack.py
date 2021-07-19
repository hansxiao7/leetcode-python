class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0

        # build the stack
        stack = [-1]
        result = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()

                if len(stack) == 0:
                    stack.append(i)
                else:
                    result = max(result, i - stack[-1])

        return result