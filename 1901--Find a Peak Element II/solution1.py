class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])

        def findRowPeak(row):
            left = 0
            right = n - 1

            while left < right:
                mid = (left + right) // 2

                if mid + 1 == n or mat[row][mid] > mat[row][mid + 1]:
                    right = mid
                elif mat[row][mid] < mat[row][mid + 1]:
                    left = mid + 1

            return left

        def findColPeak(col):
            left = 0
            right = m - 1

            while left < right:
                mid = (left + right) // 2

                if mid + 1 == m or mat[mid][col] > mat[mid + 1][col]:
                    right = mid
                elif mat[mid][col] < mat[mid + 1][col]:
                    left = mid + 1

            return left

        def checkMax(i, j):
            temp = True
            if i == 0:
                temp = temp and mat[i][j] > mat[i + 1][j]
            elif i == m - 1:
                temp = temp and mat[i][j] > mat[i - 1][j]
            else:
                temp = temp and mat[i][j] > mat[i + 1][j] and mat[i][j] > mat[i - 1][j]

            if j == 0:
                temp = temp and mat[i][j] > mat[i][j + 1]
            elif j == n - 1:
                temp = temp and mat[i][j] > mat[i][j - 1]
            else:
                temp = temp and mat[i][j] > mat[i][j - 1] and mat[i][j] > mat[i][j + 1]

            return temp

        # start with row 0
        row = 0
        while True:
            col = findRowPeak(row)
            if checkMax(row, col):
                return [row, col]

            row = findColPeak(col)
            if checkMax(row, col):
                return [row, col]
