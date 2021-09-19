class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        cache = {}

        def helper(x1, y1, x2):
            if (x1, y1, x2) in cache:
                return cache[(x1, y1, x2)]
            y2 = x1 + y1 - x2
            if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n or x2 < 0 or x2 >= m or y2 < 0 or y2 >= n:
                return -sys.maxint

            if x1 == x2 and y1 == y2 and x1 == m - 1 and y1 == n - 1:
                return grid[x1][y1]

            if grid[x1][y1] == -1:
                return -sys.maxint
            if grid[x2][y2] == -1:
                return -sys.maxint

            if x1 == x2 and y1 == y2:
                temp = grid[x1][y1]
            else:
                temp = grid[x1][y1] + grid[x2][y2]

            res = temp + max(helper(x1 + 1, y1, x2 + 1), helper(x1, y1 + 1, x2 + 1), helper(x1 + 1, y1, x2),
                             helper(x1, y1 + 1, x2))
            cache[(x1, y1, x2)] = res
            return res

        res = helper(0, 0, 0)
        if res < 0:
            return 0
        return res