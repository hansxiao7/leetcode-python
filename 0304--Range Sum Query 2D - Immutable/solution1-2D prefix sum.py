class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])

        self.prefix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix[i][j] = self.prefix[i][j - 1] + self.prefix[i - 1][j] - self.prefix[i - 1][j - 1] + \
                                    matrix[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        result = self.prefix[row2 + 1][col2 + 1] - self.prefix[row2 + 1][col1] - self.prefix[row1][col2 + 1] + \
                 self.prefix[row1][col1]

        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)