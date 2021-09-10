class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]

        res = [[1]]

        for i in range(2, numRows + 1):
            temp = []
            for j in range(i):
                if j == 0:
                    temp.append(1)
                elif j == i - 1:
                    temp.append(1)
                else:
                    temp.append(res[i - 2][j - 1] + res[i - 2][j])
            res.append(temp)

        return res