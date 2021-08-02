class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict1 = {']': '[', ')': '(', '}': '{'}

        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if dict1[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        return False