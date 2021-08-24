class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        i = 0

        while i < len(s):
            stack.append(s[i])

            if s[i] == ')':
                queue = collections.deque()
                stack.pop()
                while stack[-1] != '(':
                    queue.appendleft(stack.pop())

                stack.pop()
                stack.append(helper(queue))

            i += 1
        return helper(stack)


def helper(s):
    stack = []
    num = 0
    operator = '+'

    for i in range(len(s)):
        c = s[i]

        if isinstance(c, int) or c.isnumeric():
            num = num * 10 + int(c)

        if i == len(s) - 1 or c == '+' or c == '-' or c == '*' or c == '/':
            if operator == '+':
                stack.append(num)
            elif operator == '-':
                stack.append(-num)
            elif operator == '*':
                stack.append(stack.pop() * num)
            elif operator == '/':
                temp = stack.pop()
                if temp == 0:
                    stack.append(0)
                else:
                    stack.append(abs(temp) / abs(num) * (abs(temp) / temp) * (abs(num) / num))

            operator = c
            num = 0
    return sum(stack)
