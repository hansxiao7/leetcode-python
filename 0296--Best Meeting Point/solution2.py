class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        rows = []
        cols = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        rows.sort()
        cols.sort()

        x = rows[len(rows) // 2]
        y = cols[len(cols) // 2]

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += abs(i - x) + abs(j - y)

        return res