class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []

        def dfs(expr, pos, prev, curr):
            if pos == len(num):
                if curr == target:
                    res.append(expr)
                return

            if num[pos] == '0':
                right = 2
            else:
                right = len(num) - pos + 1

            for i in range(1, right):
                n = int(num[pos:pos + i])
                dfs(expr + '+' + str(n), pos + i, +n, curr + n)
                dfs(expr + '-' + str(n), pos + i, -n, curr - n)
                dfs(expr + '*' + str(n), pos + i, prev * n, curr - prev + prev * n)

        if num[0] == '0':
            dfs(num[:1], 1, 0, 0)
        else:
            for i in range(1, len(num) + 1):
                dfs(num[:i], i, int(num[:i]), int(num[:i]))

        return res