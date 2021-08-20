class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        lastPos = {}

        for i in range(len(s)):
            lastPos[s[i]] = i

        stack = []

        for i in range(len(s)):
            if s[i] in set(tuple(stack)):
                continue
            if len(stack) == 0 or s[i] > stack[-1]:
                stack.append(s[i])
            else:
                while len(stack) != 0 and s[i] < stack[-1] and lastPos[stack[-1]] > i:
                    stack.pop()
                stack.append(s[i])

        return ''.join(stack)