class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []
        result = 0

        for c in s:
            if c != ' ':
                stack.append(c)

            if c == ')':
                stack.pop()
                temp = 0
                while len(stack) != 0 and stack[-1] != '(':
                    pow = 1
                    curr_val = 0

                    while len(stack) != 0 and stack[-1].isnumeric():
                        curr_val += int(stack.pop()) * pow
                        pow *= 10

                    if stack[-1] == '-':
                        stack.pop()
                        temp -= curr_val
                    elif stack[-1] == '+':
                        stack.pop()
                        temp += curr_val
                    elif stack[-1] == '(':
                        temp += curr_val

                stack.pop()  # remove the '(' from the stack
                if temp >= 0:
                    stack.append(unicode(temp))
                else:
                    if len(stack) != 0 and stack[-1] == '+':
                        stack[-1] = u'-'
                        stack.append(unicode(abs(temp)))
                    elif len(stack) != 0 and stack[-1] == '-':
                        stack[-1] = u'+'
                        stack.append(unicode(abs(temp)))

        if len(stack) == 0:
            return temp

        while len(stack) != 0:
            curr_val = 0
            pow = 1
            while len(stack) != 0 and stack[-1].isnumeric():
                curr_val += int(stack.pop()) * pow
                pow *= 10

            if len(stack) != 0 and stack[-1] == '-':
                stack.pop()
                result -= curr_val

            elif len(stack) != 0 and stack[-1] == '+':
                stack.pop()
                result += curr_val
            else:
                result += curr_val

        return result
