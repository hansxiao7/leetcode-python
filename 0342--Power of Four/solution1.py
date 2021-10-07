class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = sqrt(abs(n))
        if int(temp) != temp:
            return False

        temp = int(temp)

        return n > 0 and n & (n - 1) == 0 and temp & (temp - 1) == 0