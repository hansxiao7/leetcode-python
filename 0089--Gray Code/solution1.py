class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0]
        for i in range(n):
            dp = dp + [x | 1 << i for x in reversed(dp)]
        return dp