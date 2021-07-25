class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # BFS
        m = len(grid)
        n = len(grid[0])
        queue = []
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    result += 1
                    queue = [[i, j]]
                    BFS(grid, queue)
        return result


def BFS(grid, queue):
    m = len(grid)
    n = len(grid[0])
    while len(queue) != 0:
        pos = queue.pop(0)
        x = pos[0]
        y = pos[1]
        grid[x][y] = '0'

        if x + 1 < m and grid[x + 1][y] == '1':
            queue.append([x + 1, y])
        if x - 1 >= 0 and grid[x - 1][y] == '1':
            queue.append([x - 1, y])
        if y + 1 < n and grid[x][y + 1] == '1':
            queue.append([x, y + 1])
        if y - 1 >= 0 and grid[x][y - 1] == '1':
            queue.append([x, y - 1])



