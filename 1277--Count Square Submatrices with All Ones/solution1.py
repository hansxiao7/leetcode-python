class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i - 1][j - 1] >= 1 and matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1

        result = 0
        for i in range(m):
            for j in range(n):
                result += matrix[i][j]

        return result
