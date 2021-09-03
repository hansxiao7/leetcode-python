class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """

        def helper(s):
            if s.isnumeric():
                return [int(s)]

            res = []
            for i in range(len(s)):
                if not s[i].isnumeric():
                    operator = s[i]
                    left = helper(s[:i])
                    right = helper(s[i + 1:])

                    for l in left:
                        for r in right:
                            if operator == '+':
                                res.append(l + r)
                            elif operator == '-':
                                res.append(l - r)
                            elif operator == '*':
                                res.append(l * r)
                            elif operator == '/':
                                res.append(l / r)
            return res

        return helper(expression)


