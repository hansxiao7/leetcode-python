class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        m = len(rowSum)
        n = len(colSum)

        result = [[0 for _ in range(n)] for _ in range(m)]

        def helper(x, y):
            if sum(rowSum) == 0 and sum(colSum) == 0:
                return True
            if x == m:
                return False

            if y + 1 < n:
                new_x, new_y = x, y + 1
            else:
                new_x, new_y = x + 1, 0

            for i in range(min(rowSum[x], colSum[y]) + 1):
                rowSum[x] -= i
                colSum[y] -= i
                if helper(new_x, new_y):
                    result[x][y] = i
                    return True
                result[x][y] = 0
                rowSum[x] += i
                colSum[y] += i

            return False

        helper(0, 0)
        return result