class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        # build bars
        m = len(matrix)
        n = len(matrix[0])

        bars = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            bars[0][i] = int(matrix[0][i])

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == '1':
                    bars[i][j] = bars[i - 1][j] + 1
                else:
                    bars[i][j] = 0

        result = 0
        for i in range(m):
            bar = bars[i]
            bar.append(0)
            stack = [-1]

            for j in range(len(bar)):
                while bar[j] < bar[stack[-1]]:
                    h = bar[stack.pop()]
                    w = j - stack[-1] - 1
                    result = max(result, h * w)
                stack.append(j)
        return result
