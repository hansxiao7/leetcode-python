class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def helper(x, y):
            m = len(grid2)
            n = len(grid2[0])

            if x < 0 or x >= m or y < 0 or y >= n or grid2[x][y] != 1:
                return True

            result = True
            if grid1[x][y] != 1:
                result = False
            grid2[x][y] = 2

            for i in range(len(move)):
                new_x = x + move[i][0]
                new_y = y + move[i][1]

                temp = helper(new_x, new_y)
                result = temp and result

            return result

        result = 0
        m = len(grid2)
        n = len(grid2[0])

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    temp = helper(i, j)
                    if temp:
                        result += 1

        return result
