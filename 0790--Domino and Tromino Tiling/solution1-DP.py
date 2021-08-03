class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        # totally there are 3 conditions
        f = [[0 for _ in range(3)] for _ in range(n + 1)]
        f[0][0] = 1
        f[1][0] = 1
        f[1][1] = 0
        f[1][2] = 0
        f[2][1] = 1
        f[2][2] = 1

        for i in range(2, n + 1):
            f[i][0] = f[i - 1][0] + f[i - 2][0] + f[i - 1][1] + f[i - 1][2]
            f[i][1] = f[i - 2][0] + f[i - 1][2]
            f[i][2] = f[i - 2][0] + f[i - 1][1]

        return f[n][0] % (10 ** 9 + 7)