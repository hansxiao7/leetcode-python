class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        result = [0 for _ in range(n + 1)]
        result[0] = 0
        result[1] = 1

        for i in range(2, n + 1):
            result[i] = result[i - 1] + result[i - 2]

        return result[n]