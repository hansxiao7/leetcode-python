class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i in range(len(s)):
            stack.append(s[i])

            if s[i] == ']':
                stack.pop()
                val = ''

                while stack[-1] != '[':
                    c = stack.pop()
                    val = c + val

                stack.pop()

                count = ''
                while len(stack) != 0 and stack[-1].isnumeric():
                    v = stack.pop()
                    count = v + count
                count = int(count)
                result = count * val
                stack.append(result)

        result = ''

        while len(stack) != 0:
            temp = stack.pop()
            result = temp + result

        return result