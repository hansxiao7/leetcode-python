class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 2:
            return False

        flag = False
        for i in range(2, n):
            if n % i == 0:
                if flag is False:
                    flag = True
                else:
                    return False

        return flag

