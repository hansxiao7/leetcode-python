class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        counts = {0: 1}
        # prefix for 2D
        m = len(matrix)
        n = len(matrix[0])

        prefix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + matrix[i - 1][j - 1]

        res = 0
        for i in range(m):
            for j in range(i + 1, m + 1):
                counts = {}
                for k in range(n + 1):
                    curr = prefix[j][k] - prefix[i][k]

                    if curr - target in counts:
                        res += counts[curr - target]

                    counts[curr] = counts.get(curr, 0) + 1

        return res