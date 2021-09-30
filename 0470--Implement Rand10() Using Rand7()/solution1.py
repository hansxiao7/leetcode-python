# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        num = 7 * (rand7() - 1) + rand7()
        while num > 40:
            num = 7 * (rand7() - 1) + rand7()

        res = num % 10
        if res == 0:
            return 10
        return res