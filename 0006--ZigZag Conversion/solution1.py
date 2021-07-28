class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        row = ['' for _ in range(numRows)]
        for i in range(len(s)):
            n_row = i % (2 * numRows - 2)
            if n_row + 1 > numRows:
                n_row = 2 * numRows - n_row - 2
            row[n_row] += s[i]

        result = ''

        for i in range(len(row)):
            result = result + row[i]

        return result
