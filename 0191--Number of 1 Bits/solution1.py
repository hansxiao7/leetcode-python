class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        res = 0
        while n > 0:
            res += n % 2

            n = n // 2

        return res