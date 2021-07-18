class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = final(s)
        t = final(t)

        if s == t:
            return True
        else:
            return False


def final(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '#':
            if len(stack) != 0:
                stack.pop()
        else:
            stack.append(s[i])

    return ''.join(stack)
