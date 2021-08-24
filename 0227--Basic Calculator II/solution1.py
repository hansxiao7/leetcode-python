class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        operator = '+'

        for i in range(len(s)):
            c = s[i]

            if c == ' ' and i != len(s) - 1:
                continue

            if c.isnumeric():
                num = num * 10 + int(c)

            if i == len(s) - 1 or not c.isnumeric():
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    temp = stack.pop()
                    stack.append(temp * num)
                elif operator == '/':
                    temp = stack.pop()
                    if temp == 0:
                        stack.append(0)
                    else:
                        stack.append(abs(temp) / num * (abs(temp) / temp))
                num = 0
                operator = c

        return sum(stack)