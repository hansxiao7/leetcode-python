class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        move = [-1, 0, 1]
        cache = {}

        def helper(x, y1, y2):
            if (x, y1, y2) in cache:
                return cache[(x, y1, y2)]
            if x == m:
                return 0

            if y1 < 0 or y1 >= n or y2 < 0 or y2 >= n:
                return -sys.maxint

            if y1 == y2:
                temp = grid[x][y1]
            else:
                temp = grid[x][y1] + grid[x][y2]

            nextMove = -sys.maxint
            for m1 in move:
                for m2 in move:
                    nextMove = max(nextMove, helper(x + 1, y1 + m1, y2 + m2))

            res = temp + nextMove
            cache[(x, y1, y2)] = res
            return res

        return helper(0, 0, n - 1)