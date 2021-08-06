class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """

        cache = {0: 0}

        def helper(n):
            if cache.get(n):
                return cache[n]
            if n == 0:
                return 0

            curr = 1
            result = -sys.maxint

            while curr ** 2 <= n:
                result = max(1 - helper(n - curr ** 2), result)
                curr += 1
            cache[n] = result
            return result

        result = helper(n)

        if result > 0:
            return True
        else:
            return False

