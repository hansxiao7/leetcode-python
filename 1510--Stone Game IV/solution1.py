class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pow = 1

        while pow ** 2 <= n:
            pow += 1

        cache = {}

        def helper(n, pow):
            if n in cache:
                return cache[n]
            if n == 0:
                return False

            for i in range(1, pow):
                if i ** 2 <= n:
                    temp = helper(n - i ** 2, pow)

                    if temp is False:
                        cache[n] = True
                        return True
                else:
                    break
            cache[n] = False
            return False

        return helper(n, pow)