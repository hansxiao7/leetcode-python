class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        r_index = []
        i = 0

        for i in range(len(s)):
            if s[i] != '(' and s[i] != ')':
                continue
            elif s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) != 0:
                    stack.pop()
                else:
                    r_index.append(i)

        while len(stack) != 0:
            r_index.append(stack.pop())

        r_index.sort()

        for i in range(len(r_index)):
            if r_index[i] - i + 1 < len(s):
                s = s[:r_index[i] - i] + s[r_index[i] - i + 1:]
            else:
                s = s[:r_index[i] - i]

        return s



