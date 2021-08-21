class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        def helper(s):
            stack = []
            start = None
            for i in range(len(s)):
                if s[i] == '[':
                    stack.append(i)
                elif s[i] == ']':
                    start = stack.pop()
                    end = i
                    break

            if start == None:
                return s

            val = s[start + 1:end]

            temp = start - 1
            while temp - 1 >= 0 and s[temp - 1].isnumeric():
                temp -= 1
            count = int(s[temp: start])

            result = s[:temp] + count * val + s[end + 1:]

            return helper(result)

        return helper(s)