class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        cache = [None for _ in range(n + 1)]

        def helper(n):
            if n <= 0:
                return False

            if cache[n] is not None:
                return cache[n]

            for i in range(1, 4):
                temp = helper(n - i)

                if temp is False:
                    cache[n] = True
                    return True
            cache[n] = False
            return False

        return helper(n)