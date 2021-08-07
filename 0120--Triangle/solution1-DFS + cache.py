class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # brute force
        cache = {}

        def dfs(row, prev_i, triangle):
            if cache.get((row, prev_i)):
                return cache[(row, prev_i)]
            if row == len(triangle):
                return 0

            result = sys.maxint
            for i in range(prev_i, min(len(triangle[row]), prev_i + 2)):
                result = min(result, triangle[row][i] + dfs(row + 1, i, triangle))
            cache[(row, prev_i)] = result
            return result

        result = dfs(0, 0, triangle)
        return result
