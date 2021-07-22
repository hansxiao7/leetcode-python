class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = 1
        if n < 0:
            flag = -1

        n = abs(n)

        result = helper(x, n)
        if flag == -1:
            return 1. / result
        else:
            return result


def helper(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x

    i = 1
    result = x

    while i < n:
        result = result * result
        i *= 2

    if i == n:
        return result
    else:
        return result * 1. / helper(x, i - n)
