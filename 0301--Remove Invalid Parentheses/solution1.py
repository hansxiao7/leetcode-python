class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        stack = []
        l = 0
        r = 0
        for c in s:
            if c == '(':
                stack.append('(')
            elif c == ')':
                if len(stack) != 0:
                    stack.pop()
                else:
                    r += 1

        l += len(stack)
        result = set()
        visited = set()

        def helper(l, r, s):
            if s in visited:
                return
            if l < 0 or r < 0:
                return

            if l == 0 and r == 0 and check(s):
                result.add(s)
                return
            visited.add(s)
            for i in range(len(s)):
                if i != 0 and s[i - 1] == '(':
                    if s[i] == ')' and r > 0:
                        helper(l, r - 1, s[:i] + s[i + 1:])
                elif i != 0 and s[i - 1] == ')':
                    if s[i] == '(' and r == 0:
                        helper(l - 1, r, s[:i] + s[i + 1:])
                else:
                    if r > 0:
                        helper(l, r - 1, s[:i] + s[i + 1:])
                    else:
                        helper(l - 1, r, s[:i] + s[i + 1:])

        helper(l, r, s)
        return result


def check(s):
    res = 0

    for c in s:
        if c == '(':
            res += 1
        elif c == ')':
            if res > 0:
                res -= 1
            else:
                return False

    if res == 0:
        return True
    return False