class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        f = [[0 for _ in range(2)] for _ in range(n)]

        if s[0] == '0':
            f[0][0] = 0
            f[0][1] = 1
        else:
            f[0][0] = 1
            f[0][1] = 0

        for i in range(1, n):
            if s[i] == '0':
                f[i][0] = f[i - 1][0]
                f[i][1] = min(f[i - 1][0], f[i - 1][1]) + 1
            else:
                f[i][1] = min(f[i - 1][0], f[i - 1][1])
                f[i][0] = 1 + f[i - 1][0]

        return min(f[n - 1])