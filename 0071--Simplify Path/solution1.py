class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []

        i = 0

        while i < len(path):
            start = i

            while i < len(path) - 1 and path[i + 1] != '/':
                i += 1

            temp = path[start:i + 1]

            if temp == '/' or temp == '/.':
                i += 1
                continue
            elif temp == '/..':
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(temp)

            i += 1

        result = ''.join(stack)

        if result == '':
            result = '/'
        return result