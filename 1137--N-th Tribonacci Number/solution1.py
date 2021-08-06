class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        x1 = 0
        x2 = 1
        x3 = 1

        for i in range(3, n + 1):
            temp = x1 + x2 + x3

            x1 = x2
            x2 = x3
            x3 = temp
        return temp