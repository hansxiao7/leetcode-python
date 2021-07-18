class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        result = set()
        li = ['(']
        li = generate_list(2 * n - 1, li)
        for i in range(len(li)):
            if true_string(li[i]):
                result.add(li[i])

        return result


def true_string(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
                continue

    if len(stack) == 0:
        return True
    else:
        return False


def generate_list(n, li):
    if n == 0:
        return li
    else:
        temp1 = []
        temp2 = []
        for i in range(len(li)):
            temp1.append(li[i] + '(')
            temp2.append(li[i] + ')')
        temp1.extend(temp2)
        return generate_list(n - 1, temp1)
