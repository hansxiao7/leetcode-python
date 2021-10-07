class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = {}
        for c in s:
            counts[c] = counts.get(c, -1) + 1

        stack = []

        for c in s:
            if c in set(tuple(stack)):
                counts[c] -= 1
                continue
            while len(stack) != 0 and c <= stack[-1]:
                if counts[stack[-1]] > 0:
                    counts[stack[-1]] -= 1
                    stack.pop()
                else:
                    break

            stack.append(c)

        return ''.join(stack)