class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        temp = [1]
        for i in range(1, rowIndex + 1):
            newRow = [1] * (i + 1)
            for j in range(1, i):
                newRow[j] = temp[j] + temp[j - 1]

            temp = newRow

        return temp