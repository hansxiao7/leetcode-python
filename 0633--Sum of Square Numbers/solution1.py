class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l = 0
        r = int(c ** 0.5)
        while l <= r:
            curr = l*l + r*r
            if curr < c:
                l += 1
            elif curr > c:
                r -= 1
            else:
                return True
        return False