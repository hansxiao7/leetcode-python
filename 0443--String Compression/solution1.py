class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(chars)):

            if (i > 0 and chars[i] != chars[i - 1]):
                c = chars[i - 1]
                count = 0
                while len(stack) != 0 and stack[-1] == c:
                    stack.pop()
                    count += 1
                stack.append(c)
                if count > 1:
                    for tempC in str(count):
                        stack.append(int(tempC))
            stack.append(chars[i])

        c = stack.pop()
        count = 1
        while len(stack) != 0 and stack[-1] == c:
            stack.pop()
            count += 1

        stack.append(c)
        if count > 1:
            for tempC in str(count):
                stack.append(int(tempC))

        pos = 0
        for i in range(len(stack)):
            chars[i] = str(stack[i])
        return len(stack)