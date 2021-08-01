class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        sign = abs(x) / x

        result = 0
        num = abs(x)

        while num != 0:
            result = result * 10 + num % 10
            num = num // 10

        result = sign * result
        if result < - 2 ** 31 or result > 2 ** 31 - 1:
            return 0
        return result