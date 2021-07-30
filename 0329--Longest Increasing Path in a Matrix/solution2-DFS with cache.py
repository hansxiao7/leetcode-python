class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # DFS - brute force
        m = len(matrix)
        n = len(matrix[0])

        result = 1
        cache = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j, -sys.maxint, matrix, cache))

        return result


def dfs(x, y, prev, matrix, cache):
    m = len(matrix)
    n = len(matrix[0])

    if x < 0 or x >= m or y < 0 or y >= n:
        return 0

    if matrix[x][y] <= prev:
        return 0

    if cache[x][y] != 0:
        return cache[x][y]

    temp1 = 1 + dfs(x - 1, y, matrix[x][y], matrix, cache)
    temp2 = 1 + dfs(x + 1, y, matrix[x][y], matrix, cache)
    temp3 = 1 + dfs(x, y - 1, matrix[x][y], matrix, cache)
    temp4 = 1 + dfs(x, y + 1, matrix[x][y], matrix, cache)

    result = max(temp1, temp2, temp3, temp4)
    cache[x][y] = result

    return result