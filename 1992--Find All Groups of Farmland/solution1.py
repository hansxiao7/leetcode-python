class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        m = len(land)
        n = len(land[0])

        def helper(x, y, x1, y1, x2, y2):
            if x < 0 or x >= m or y < 0 or y >= n or land[x][y] != 1:
                return x1, y1, x2, y2

            x1 = min(x1, x)
            x2 = max(x2, x)
            y1 = min(y1, y)
            y2 = max(y2, y)

            land[x][y] = 0

            u = helper(x - 1, y, x1, y1, x2, y2)
            d = helper(x + 1, y, x1, y1, x2, y2)
            l = helper(x, y - 1, x1, y1, x2, y2)
            r = helper(x, y + 1, x1, y1, x2, y2)

            x1 = min(x1, u[0], d[0], l[0], r[0])
            y1 = min(y1, u[1], d[1], l[1], r[1])
            x2 = max(x2, u[2], d[2], l[2], r[2])
            y2 = max(y2, u[3], d[3], l[3], r[3])

            return x1, y1, x2, y2

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    result.append(helper(i, j, i, j, i, j))

        return result