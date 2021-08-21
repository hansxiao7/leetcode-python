class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        def helper(s):
            stack = []
            start = None
            i = 0
            while i < len(s):
                if s[i] == '[':
                    stack.append(i)
                elif s[i] == ']':
                    start = stack.pop()
                    end = i
                    val = s[start + 1:end]
                    temp = start - 1
                    while temp - 1 >= 0 and s[temp - 1].isnumeric():
                        temp -= 1
                    count = int(s[temp: start])

                    s = s[:temp] + count * val + s[end + 1:]
                    i = temp + count - 1
                i += 1

            return s

        return helper(s)