class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return k
        if n == 2:
            return k * k
        f = [0 for _ in range(n + 1)]
        f[1] = k
        f[2] = k * k

        for i in range(3, n + 1):
            f[i] = (k - 1) * (f[i - 1] + f[i - 2])

        return f[n]