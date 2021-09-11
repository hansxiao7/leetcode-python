class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        plus = 0
        mul = 1
        while n != 0:
            plus += n % 10
            mul = mul * (n % 10)
            n = n // 10

        return mul - plus