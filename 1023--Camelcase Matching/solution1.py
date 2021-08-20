class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """

        def helper(x, y):
            if x == '' and y == '':
                return True
            elif y == '':
                temp = ord(x[-1]) - ord('a')
                if temp >= 0 and temp < 26:
                    return helper(x[:len(x) - 1], y)
                else:
                    return False
            elif x == '':
                return False

            if x[-1] == y[-1]:
                return helper(x[:len(x) - 1], y[:len(y) - 1])
            else:
                temp = ord(x[-1]) - ord('a')
                if temp >= 0 and temp < 26:
                    return helper(x[:len(x) - 1], y)
                else:
                    return False

        result = []

        for q in queries:
            result.append(helper(q, pattern))

        return result