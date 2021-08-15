class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        # dfs + cache
        cache = {}

        def helper(x, y, nMove, m, n):
            if (x, y, nMove) in cache:
                return cache[(x, y, nMove)]
            if nMove < 0:
                return 0

            if x < 0 or x >= m or y < 0 or y >= n:
                return 1

            temp1 = helper(x + 1, y, nMove - 1, m, n)
            temp2 = helper(x - 1, y, nMove - 1, m, n)
            temp3 = helper(x, y + 1, nMove - 1, m, n)
            temp4 = helper(x, y - 1, nMove - 1, m, n)

            result = temp1 + temp2 + temp3 + temp4
            cache[(x, y, nMove)] = result
            return result

        return helper(startRow, startColumn, maxMove, m, n) % (10 ** 9 + 7)