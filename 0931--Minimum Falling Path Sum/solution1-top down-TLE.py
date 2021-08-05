class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # brute force
        self.result = sys.maxint

        def helper(row, prev_y, curr):
            m = n = len(matrix)

            if row == m:
                if curr < self.result:
                    self.result = curr
                return

            if prev_y is not None:
                left = prev_y - 1
                right = prev_y + 1
            else:
                left = 0
                right = n - 1

            for i in range(left, right + 1):
                if i < 0 or i >= n:
                    continue
                helper(row + 1, i, curr + matrix[row][i])

        helper(0, None, 0)
        return self.result
