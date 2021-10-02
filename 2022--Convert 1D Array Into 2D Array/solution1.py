class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if m * n != len(original):
            return []
        res = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(len(original)):
            x = i // n
            y = i % n

            res[x][y] = original[i]

        return res