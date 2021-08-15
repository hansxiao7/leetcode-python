class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        if k == 0:
            return 1
        pos = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        cache = {}

        def helper(x, y, n, k):
            if (x, y, k) in cache:
                return cache[(x, y, k)]
            if x < 0 or x >= n or y < 0 or y >= n:
                return 0

            if k == 0:
                return 1

            result = 0
            for dx, dy in pos:
                result += helper(x + dx, y + dy, n, k - 1)
            cache[(x, y, k)] = result
            return result

        result = helper(row, column, n, k)
        return result / float(8 ** k)
