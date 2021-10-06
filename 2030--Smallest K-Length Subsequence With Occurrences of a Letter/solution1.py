class Solution(object):
    def smallestSubsequence(self, s, k, letter, repetition):
        """
        :type s: str
        :type k: int
        :type letter: str
        :type repetition: int
        :rtype: str
        """
        counts = 0
        for c in s:
            if c == letter:
                counts += 1

        stack = []

        k1 = 0
        k2 = 0

        for c in s:
            # len(s) - k
            # counts - repetition
            while len(stack) != 0 and c < stack[-1]:
                if stack[-1] == letter:
                    if k2 < counts - repetition and k1 < len(s) - k:
                        k1 += 1
                        k2 += 1
                        stack.pop()
                    else:
                        break
                else:
                    if k1 < len(s) - k:
                        k1 += 1
                        stack.pop()
                    else:
                        break

            stack.append(c)

        temp = 0
        while k1 < len(s) - k:
            if stack[-1] == letter:
                if k2 < counts - repetition:
                    stack.pop()
                    k1 += 1
                    k2 += 1
                else:
                    temp += 1
                    stack.pop()
            else:
                k1 += 1
                stack.pop()

        return ''.join(stack) + temp * letter

